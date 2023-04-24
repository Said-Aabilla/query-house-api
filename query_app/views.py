from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Query
from .serializers import QuerySerializer

class QueryList(generics.ListCreateAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer

class QueryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Query.objects.all()
    serializer_class = QuerySerializer
