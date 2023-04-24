from django.db import models

from app.models_base import BaseModel


class Query(BaseModel):
    query = models.CharField(max_length=500)
    join_order = models.CharField(max_length=250)
    execution_time = models.FloatField(null=True)
    estimated_execution_time = models.FloatField(null=True)
    execution_energy = models.FloatField(null=True)
    tables = models.ManyToManyField('Table')
    selections = models.ManyToManyField('Selection')
    projections = models.ManyToManyField('Projection')
    joins = models.ManyToManyField('Join')


class Table(BaseModel):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    queries = models.ManyToManyField('Query')


class Attribute(BaseModel):
    name = models.CharField(max_length=50)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='attributes')


class Selection(models.Model):
    selection = models.CharField(max_length=255)
    queries = models.ManyToManyField(Query)
    algorithm = models.ForeignKey('SelectionAlgorithm', on_delete=models.CASCADE, related_name='selections')
    operators = models.ManyToManyField('Operator', through='SelectionOperator')
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='selections')


class Operator(models.Model):
    name = models.CharField(max_length=50)


class Value(models.Model):
    value = models.CharField(max_length=255)
    domain = models.ForeignKey('Domain', on_delete=models.CASCADE, related_name='values')


class Domain(models.Model):
    name = models.CharField(max_length=255)


class SelectionOperator(models.Model):
    selection = models.ForeignKey(Selection, on_delete=models.CASCADE)
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    value = models.ForeignKey(Value, on_delete=models.CASCADE, related_name='selectionOperators')


class SelectionAlgorithm(models.Model):
    name = models.CharField(max_length=255)


class Projection(models.Model):
    projection = models.CharField(max_length=255)
    all = models.BooleanField(null=True)
    queries = models.ManyToManyField(Query)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE, related_name='projections')


class Aggregation(models.Model):
    function = models.CharField(max_length=255)
    projection = models.ForeignKey(Projection, on_delete=models.CASCADE, related_name='aggregations')


class Join(models.Model):
    join = models.CharField(max_length=255)
    index = models.ForeignKey('JoinIndex', on_delete=models.CASCADE, related_name='joins')
    algorithm = models.ForeignKey('JoinAlgorithm', on_delete=models.CASCADE, related_name='joins')
    queries = models.ManyToManyField(Query)


class JoinAttribute(models.Model):
    join = models.ForeignKey(Join, on_delete=models.CASCADE)
    attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
    position = models.CharField(max_length=20)


class joinAlgorithm(models.Model):
    name = models.CharField(max_length=255)


class JoinIndex(models.Model):
    name = models.CharField(max_length=255)
