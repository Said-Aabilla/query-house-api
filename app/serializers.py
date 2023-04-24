from rest_framework import serializers
from .models import Query, Table

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'name']

class QuerySerializer(serializers.ModelSerializer):
    tables = TableSerializer(many=True)

    class Meta:
        model = Query
        fields = ['id', 'name', 'tables']
