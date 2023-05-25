from rest_framework import serializers
from app.models import Query, Table, Selection, Projection, Join,Attribute,Operator,Value,Domain

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'name','attributes' ]

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ['id', 'name', 'table']
class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ['value', 'domain']
class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ['domain']
class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ['name']
class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = [

            'id', 'selection', 'algorithm', 'operators', 'attribute','sf','attr']


class ProjectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projection
        fields = ['id', 'projection', 'all',  'attribute','aggregation_id']

class JoinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Join
        fields = ['id', 'join', 'index', 'algorithm']
class CreateQuerySerializer(serializers.ModelSerializer):
    tables = TableSerializer(many=True, read_only=True)
    selections = SelectionSerializer(many=True, read_only=True)
    projections = ProjectionSerializer(many=True, read_only=True)
    joins = JoinSerializer(many=True, read_only=True)
    class Meta:
        model = Query
        fields = ['query', 'tables', 'selections', 'projections', 'joins']
class QuerySerializer(serializers.ModelSerializer):
    tables = TableSerializer(many=True, read_only=True)
    selections = SelectionSerializer(many=True, read_only=True)
    projections = ProjectionSerializer(many=True, read_only=True)
    joins = JoinSerializer(many=True, read_only=True)
    class Meta:
        model = Query
        fields = ['id', 'query',
                  'number_join',

       'converge',
       'prefix',
        'join_order_pg',
        'choosed_plan',
        'join_order_hinter',
        'prefix_algo',
        'execution_time_hybride',
        'execution_time_pg',
        'execution_energy_pg',
        'execution_energy_hybrid',
        'tables', 'selections', 'projections', 'joins']

class AddDatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ['dbname','dbuser','dbpassword','dbport']
