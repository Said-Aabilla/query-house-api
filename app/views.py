from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, status
from rest_framework.response import Response

from .models import Query, Table, SelectionAlgorithm, Attribute, Selection, Operator, Value, SelectionOperator, \
    Projection, Aggregation, JoinIndex, Join, JoinAttribute, JoinAlgorithm
from .serializers import QuerySerializer

class QueryViewSet(viewsets.ModelViewSet):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

    def search(self, request):
        keyword = request.GET.get('keyword')
        queries = Query.objects.filter(query__icontains=keyword)
        serializer = QuerySerializer(queries, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        table_data = request.data.pop('tables')
        selections_data = request.data.pop('selections')
        projections_data = request.data.pop('projections')
        joins_data = request.data.pop('joins')

        # create Query object
        query = Query.objects.create(**request.data)

        # create Table objects and add to Query
        tables = []
        for table in table_data:
            tables.append(Table.objects.create(**table))
        query.tables.set(tables)

        # create Selection objects and add to Query
        selections = []
        for selection in selections_data:
            algorithm_data = selection.pop('algorithm')
            operators_data = selection.pop('operators')
            attribute_data = selection.pop('attribute')
            algorithm = SelectionAlgorithm.objects.create(**algorithm_data)
            attribute = Attribute.objects.create(**attribute_data)
            selection_obj = Selection.objects.create(query=query, algorithm=algorithm, attribute=attribute, **selection)
            operators = []
            for operator_data in operators_data:
                value_data = operator_data.pop('value')
                operator = Operator.objects.create(**operator_data)
                value = Value.objects.create(**value_data)
                operators.append(SelectionOperator.objects.create(selection=selection_obj, operator=operator, value=value))
            selections.append(selection_obj)
        query.selections.set(selections)

        # create Projection objects and add to Query
        projections = []
        for projection in projections_data:
            attribute_data = projection.pop('attribute')
            attribute = Attribute.objects.create(**attribute_data)
            projection_obj = Projection.objects.create(query=query, attribute=attribute, **projection)
            aggregations_data = projection.pop('aggregations')
            for aggregation_data in aggregations_data:
                Aggregation.objects.create(projection=projection_obj, **aggregation_data)
            projections.append(projection_obj)
        query.projections.set(projections)

        # create Join objects and add to Query
        joins = []
        for join in joins_data:
            index_data = join.pop('index')
            algorithm_data = join.pop('algorithm')
            index = JoinIndex.objects.create(**index_data)
            algorithm = JoinAlgorithm.objects.create(**algorithm_data)
            join_obj = Join.objects.create(query=query, index=index, algorithm=algorithm, **join)
            join_attributes_data = join.pop('joinattributes')
            for join_attribute_data in join_attributes_data:
                attribute_data = join_attribute_data.pop('attribute')
                attribute = Attribute.objects.create(**attribute_data)
                JoinAttribute.objects.create(join=join_obj, attribute=attribute, **join_attribute_data)
            joins.append(join_obj)
        query.joins.set(joins)

        serializer = QuerySerializer(query)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
