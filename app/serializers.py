from rest_framework import serializers
from app.models import Query, Table, Selection, Projection, Join


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'name', 'alias', 'queries']


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ['id', 'selection', 'queries', 'algorithm', 'operators', 'attribute']


class ProjectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projection
        fields = ['id', 'projection', 'all', 'queries', 'attribute']


class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Join
        fields = ['id', 'join', 'index', 'algorithm', 'queries']


class QuerySerializer(serializers.ModelSerializer):
    tables = TableSerializer(many=True, read_only=True)
    selections = SelectionSerializer(many=True, read_only=True)
    projections = ProjectionSerializer(many=True, read_only=True)
    joins = JoinSerializer(many=True, read_only=True)

    class Meta:
        model = Query
        fields = ['id', 'query', 'join_order', 'execution_time', 'estimated_execution_time', 'execution_energy',
                  'tables', 'selections', 'projections', 'joins']
