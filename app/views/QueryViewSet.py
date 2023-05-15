import json

from django.shortcuts import get_object_or_404
from django.template.defaultfilters import upper
from rest_framework import viewsets
from rest_framework.response import Response

from app.models import Query, Table, Selection, Operator, Value, Aggregation, Projection, Join, Attribute, JoinAttribute
from app.serializers import CreateQuerySerializer, QuerySerializer
class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
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
        execution_time_hybride = data.get('execution_time_hybride')
        execution_time_pg = data.get('execution_time_pg')

        join_order_pg = data.get('join_order_pg')
        converge = data.get('converge')
        join_order_hinter = data.get('join_order_hinter')
        choosed_plan = data.get('choosed_plan')
        number_join = data.get('number_join')
        prefix_algo = data.get('prefix_algo')
        execution_energy_hybrid = data.get('execution_energy_hybrid')
        json_plan_pg = data.get('json_plan_pg')
        json_plan_hinter= data.get('json_plan_hybride')
        execution_energy_pg = data.get('execution_energy_pg')
        json_plan_hinter_real = data.get('json_plan_hinter_real')
        json_plan_pg_real = data.get('json_plan_pg_real')
        prefix = data.get('prefix')
        # Create the Query object
        query = Query.objects.create(query=query_str,
                                     json_plan_hinter_real = json_plan_hinter_real,
                                     json_plan_pg_real= json_plan_pg_real,
                                     json_plan_hinter = json_plan_hinter,
                                     json_plan_pg = json_plan_pg,
                                     number_join= number_join,
                                     execution_time_hybride=execution_time_hybride,
                                     execution_time_pg=execution_time_pg,
                                     converge = converge,
                                     prefix_algo=prefix_algo,
                                     execution_energy_hybrid=execution_energy_hybrid,
                                     execution_energy_pg=execution_energy_pg,
                                     join_order_pg=join_order_pg,
                                     join_order_hinter=join_order_hinter,
                                     choosed_plan=choosed_plan,

        prefix=prefix,
                                )
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
                print(op_info)
                operator = Operator.objects.get(name=op_info['operator'])
                value = Value.objects.create(value=op_info['value'], domain_id=op_info['domain_id'])
                selection.operators.add(operator, through_defaults={'value': value})
        # Add the projections to the query
        for proj in projection_info:
            # Add the aggregation to the projection
            aggregation = Aggregation.objects.get(function=upper(proj['aggregation']))
            projection = Projection.objects.create(projection=proj['projection'], alias=proj['alias'],
                                                   all=proj['all'], attribute_id=proj['attribute_id'],
                                                   aggregation=aggregation)
            query.projections.add(projection)
        # Add the joins to the query
        for join_info in join_info:
            join = Join.objects.create(join=join_info['join'])
            # Add the attributes to the join
            print('c',join_info)
            for join_attr_info in join_info['join_attributes']:
                attribute = Attribute.objects.get(id=join_attr_info['attribute_id'])
                JoinAttribute.objects.create(join=join, attribute=attribute, position=join_attr_info['position'])
            query.joins.add(join)
        serializer = QuerySerializer(query)
        return Response(serializer.data)
    def updateJoinOrder(self, request, *args, **kwargs):
        data = json.loads(request.body)
        query_id = data.get('queryId')
        join_order = data.get('joinOrder')

        # Get the Query object
        try:
            query = Query.objects.filter(id=query_id).first()
            if not query:
                return Response({'error': 'Query object not found.'}, status=404)
        except ValueError:
            return Response({'error': 'Invalid query ID.'}, status=400)
        # Verify the join order is not empty
        if not join_order:
            return Response({'error': 'Join order cannot be empty.'}, status=400)

        query.join_order = join_order

        query.save()

        serializer = QuerySerializer(query)

        return Response(serializer.data)