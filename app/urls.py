from django.urls import include, path
from rest_framework import routers
from app.views import QueryViewSet, ProjectionRetrieveUpdateDestroyAPIView, \
    ProjectionCreateAPIView, AttributeCreateAPIView, AttributeRetrieveUpdateDestroyAPIView, TableCreateAPIView, \
    TableRetrieveUpdateDestroyAPIView, OperatorCreateAPIView, OperatorRetrieveUpdateDestroyAPIView, DomainCreateAPIView, \
    DomainRetrieveUpdateDestroyAPIView, DatabaseHandler

router = routers.DefaultRouter()
router.register(r'queries', QueryViewSet)
router.register(r'database', DatabaseHandler)
urlpatterns = [
    path('', include(router.urls)),
    path('queries/search/', QueryViewSet.as_view({'get': 'search'}), name='query_search'),
    path('projections/', ProjectionCreateAPIView.as_view(), name='projection-create'),
    path('projections/<int:pk>/', ProjectionRetrieveUpdateDestroyAPIView.as_view(), name='projection-retrieve-update-destroy'),
    path('attributes/', AttributeCreateAPIView.as_view(), name='attribute-create'),
    path('attributes/<int:pk>/', AttributeRetrieveUpdateDestroyAPIView.as_view(), name='attribute-retrieve-update-destroy'),
    path('tables/', TableCreateAPIView.as_view(), name='table-create'),
    path('tables/<int:pk>/', TableRetrieveUpdateDestroyAPIView.as_view(), name='table-retrieve-update-destroy'),
    path('operators/', OperatorCreateAPIView.as_view(), name='operator-create'),
    path('operators/<int:pk>/', OperatorRetrieveUpdateDestroyAPIView.as_view(), name='operator-retrieve-update-destroy'),
    path('domains/', DomainCreateAPIView.as_view(), name='domain-create'),
    path('domains/<int:pk>/', DomainRetrieveUpdateDestroyAPIView.as_view(), name='domain-retrieve-update-destroy'),
    path('database/add', DatabaseHandler.as_view({'post':'post'}), name='database-route'),

]
