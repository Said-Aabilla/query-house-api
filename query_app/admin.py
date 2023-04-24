from django.contrib import admin

# Register your models here.
from .models import Query, Table

admin.site.register(Query)
admin.site.register(Table)