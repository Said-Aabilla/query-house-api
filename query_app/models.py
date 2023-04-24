from django.db import models

from query_app.models_base import BaseModel


class Table(BaseModel):
    name = models.CharField(max_length=255)
    # add any other fields you need

class Query(BaseModel):
    name = models.CharField(max_length=255)
    tables = models.ManyToManyField(Table)
    # add any other fields you need