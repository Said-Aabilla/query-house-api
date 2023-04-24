from django.urls import path
from .views import QueryList, QueryDetail

urlpatterns = [
    path('queries/', QueryList.as_view(), name='query-list'),
    path('queries/<int:pk>/', QueryDetail.as_view(), name='query-detail'),
]
