import json
import logging
logging.basicConfig(level=logging.DEBUG)
import psycopg2
from rest_framework import viewsets
from rest_framework.response import Response

from app.models import Query, Table, Alias, Attribute, JoinAlgorithm, Operator, Aggregation, SelectionAlgorithm
from app.serializers import AddDatabaseSerializer, TableSerializer


class DatabaseHandlerView(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = AddDatabaseSerializer

    def post(self, request):
        data = json.loads(request.body)
        joinAlgorithms = data.get('joinAlgorithms')
        aggreations = data.get('aggreations')
        operations = data.get('operations')
        selectionAlgorithms = data.get('selectionAlgorithms')

        conn = psycopg2.connect(
            host=data.get("dbhost"),
            port=data.get('dbport'),
            database=data.get('dbname'),
            user=data.get('dbuser'),
            password=data.get('dbpassword'))
        cur = conn.cursor()
        cur.execute("""
            SELECT table_name, column_name, data_type
            FROM information_schema.columns
            WHERE table_schema = 'public'
            ORDER BY table_name, ordinal_position;
        """)
        rows = cur.fetchall()
        result = []
        aliases_dict = data.get('aliases')
        my_dict = {}
        for row in rows:
            table_name, column_name, data_type = row
            result.append({'table_name': table_name, 'column_name': column_name, 'data_type': data_type})
        for record in result:
            resultTable = Table.objects.filter(name=record.get('table_name'))
            # table d'ont exist
            if len(resultTable) == 0:
                resultInsertionTable = Table.objects.create(name=record.get('table_name'))
                list_aliases = aliases_dict.get(record.get('table_name'))
                Attribute.objects.create(name=record.get('column_name'), table_id=resultInsertionTable.id)
                for alias in list_aliases:
                    Alias.objects.create(name=alias, table_id=resultInsertionTable.id)
            if len(resultTable) > 0:
                if len(Attribute.objects.filter(name=record.get('column_name'), table_id=resultTable[0].id)) == 0:
                    Attribute.objects.create(name=record.get('column_name'), table_id=resultTable[0].id)
        querySet = Table.objects.prefetch_related('attributes').all()
        for join in joinAlgorithms:
            if len(JoinAlgorithm.objects.filter(name=join)) == 0:
                JoinAlgorithm.objects.create(name=join)
        for operation in operations:
            if len(Operator.objects.filter(name=operation)) == 0:
                Operator.objects.create(name=operation)
        for aggreation in aggreations:
            if len(Aggregation.objects.filter(function=aggreation)) == 0:
                Aggregation.objects.create(function=aggreation)
        for selectionAlgorithm in selectionAlgorithms:
            if len(SelectionAlgorithm.objects.filter(name=selectionAlgorithm)) == 0:
                SelectionAlgorithm.objects.create(name=selectionAlgorithm)
        serializer = TableSerializer(querySet, many=True)
        # Return the dictionary as JSON response
        return Response(serializer.data)
