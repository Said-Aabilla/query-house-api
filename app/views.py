import json
import logging

from django.forms import model_to_dict
from django.http import JsonResponse
from django.views import View

logging.basicConfig(level=logging.DEBUG)
import psycopg2
import json
from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
def get_attribute(request, table_id, attribute_name):
    table = get_object_or_404(Table, id=table_id)
    attribute = get_object_or_404(Attribute, name=attribute_name, table=table)
    data = {
        'name': attribute.name,
        'table': attribute.table.id,
        'attribute_id': attribute.id
    }
    return JsonResponse(data)
def get_table(request, table_name, ):
    print('lign 26')
    table = get_object_or_404(Table,name=table_name)
    data = {
        'table_id': table.id,
        'table_name': table_name,
    }
    return JsonResponse(data)
from .models import Query, Table, SelectionAlgorithm, Attribute, Selection, Operator, Value, SelectionOperator, \
    Projection, Aggregation, JoinIndex, Join, JoinAttribute, JoinAlgorithm, Domain,Alias
from .serializers import ProjectionSerializer, AttributeSerializer, TableSerializer, \
    OperatorSerializer, ValueSerializer, DomainSerializer, CreateQuerySerializer, QuerySerializer, AddDatabaseSerializer
class DatabaseHandler(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = AddDatabaseSerializer

    def post(self, request):
        data = json.loads(request.body)
        joinAlgorithms = data.get('joinAlgorithms')
        aggreations = data.get('aggreations')
        operations = data.get('operations')
        selectionAlgorithms= data.get('selectionAlgorithms')

        conn = psycopg2.connect(
            host=data.get("dbhost"),
            port=data.get('dbport'),
            database=data.get('dbname'),
            user=data.get('dbuser'),
            password=data.get('password'))
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
                resultInsertionTable = Table.objects.create(name=record.get('table_name'),)
                list_aliases = aliases_dict.get(record.get('table_name'))
                for alias  in list_aliases:
                    Alias.objects.create(name=alias,table_id=resultInsertionTable.id)
            if len(resultTable) > 0:
                if len(Attribute.objects.filter(name=record.get('column_name'),table_id=resultTable[0].id))==0:
                    Attribute.objects.create(name=record.get('column_name'),table_id=resultTable[0].id)
        querySet = Table.objects.prefetch_related('attributes').all()
        for join in joinAlgorithms:
            if len(JoinAlgorithm.objects.filter(name=join)) == 0:
                JoinAlgorithm.objects.create(name=join)
        for operation in operations:
            if len(Operator.objects.filter(name=operation)) == 0:
                Operator.objects.create(name=operation)
        for aggreation in aggreations:
            if len( Aggregation.objects.filter(function=aggreation)) == 0:
                Aggregation.objects.create(function=aggreation)
        for selectionAlgorithm in selectionAlgorithms:
            if len(SelectionAlgorithm.objects.filter(name=selectionAlgorithm)) == 0:
                SelectionAlgorithm.objects.create(name=selectionAlgorithm)
        serializer = TableSerializer(querySet,many=True)
        # Return the dictionary as JSON response
        return Response(serializer.data)
class DomainCreateAPIView(generics.CreateAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer
class DomainRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainSerializer


class ValueCreateAPIView(generics.CreateAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer


class ValueRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer


class TableCreateAPIView(generics.CreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class OperatorCreateAPIView(generics.CreateAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer


class OperatorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer


class AttributeCreateAPIView(generics.CreateAPIView):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


class AttributeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projection.objects.all()
    serializer_class = AttributeSerializer


class ProjectionCreateAPIView(generics.CreateAPIView):
    queryset = Projection.objects.afirst()
    serializer_class = ProjectionSerializer


class ProjectionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projection.objects.all()
    serializer_class = ProjectionSerializer


class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = CreateQuerySerializer

    def search(self, request):
        keyword = request.GET.get('keyword')
        queries = Query.objects.filter(query__icontains=keyword)
        serializer = QuerySerializer(queries, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):

        data = json.loads(request.body)
        query_str = data.get('query')
        table_ids = data.get('table', [])
        selection_info = data.get('selection', [])
        projection_info = data.get('projection', [])
        join_info = data.get('join', [])

        # Create the Query object
        query = Query.objects.create(query=query_str)

        # Add the tables to the query
        for table_id in table_ids:
            table = Table.objects.get(id=table_id)
            query.tables.add(table)

        # Add the selections to the query
        for sel in selection_info:
            selection = Selection.objects.create(selection=sel['selection'], attribute_id=sel['attribute_id'])
            query.selections.add(selection)

            # Add the operators and values to the selection
            for op_info in sel['operators']:
                operator = Operator.objects.get(name=op_info['operator'])
                value = Value.objects.create(value=op_info['value'], domain_id=op_info['domain_id'])
                selection.operators.add(operator, through_defaults={'value': value})

        # Add the projections to the query
        for proj in projection_info:
            # Add the aggregation to the projection

            aggregation = Aggregation.objects.get(function=proj['aggregation'])

            projection = Projection.objects.create(projection=proj['projection'], alias=proj['alias'],
                                                   all=proj['all'], attribute_id=proj['attribute_id'],
                                                   aggregation=aggregation)

        # Add the joins to the query
        for join_info in join_info:
            join = Join.objects.create(join=join_info['join'])

            # Add the attributes to the join
            for join_attr_info in join_info['join_attributes']:
                attribute = Attribute.objects.get(id=join_attr_info['attribute_id'])
                JoinAttribute.objects.create(join=join, attribute=attribute, position=join_attr_info['position'])

            query.joins.add(join)

        serializer = QuerySerializer(query)

        return Response(serializer.data)
