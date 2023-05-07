from django.urls import include, path
from rest_framework import routers

from app.views.DatabaseHandlerView import DatabaseHandlerView
from app.views.QueryViewSet import QueryViewSet
from app.views.views import findAttributeByNameAndTable, findTableByName

router = routers.DefaultRouter()
router.register(r'queries', QueryViewSet)
router.register(r'database', DatabaseHandlerView)
urlpatterns = [
    path('', include(router.urls)),
    path('database/add', DatabaseHandlerView.as_view({'post': 'post'}), name='database-route'),
    path('queries/search/', QueryViewSet.as_view({'get': 'search'}), name='query_search'),
    path('queries/updateJoinOrder', QueryViewSet.as_view({'put': 'updateJoinOrder'}), name='updateJoinOrder'),
    path('tables/<str:table_name>/attributes/<str:attribute_name>/', findAttributeByNameAndTable,
         name='findAttributeByNameAndTable'),
    path('tables/<str:table_name>/', findTableByName, name='get_table')

]
