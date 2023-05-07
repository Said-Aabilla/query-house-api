import logging

from django.http import JsonResponse

logging.basicConfig(level=logging.DEBUG)
from django.shortcuts import get_object_or_404
from app.models import Table, Attribute


def findAttributeByNameAndTable(request, table_name, attribute_name):
    table = get_object_or_404(Table, name=table_name)
    attribute = get_object_or_404(Attribute, name=attribute_name, table=table)
    data = {
        'name': attribute.name,
        'table': attribute.table.id,
        'attribute_id': attribute.id
    }
    return JsonResponse(data)


def findTableByName(request, table_name, ):
    print('lign 26')
    table = get_object_or_404(Table, name=table_name)
    data = {
        'table_id': table.id,
        'table_name': table_name,
    }
    return JsonResponse(data)
