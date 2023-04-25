from django.urls import include, path
from rest_framework import routers
from app.views import QueryViewSet

router = routers.DefaultRouter()
router.register(r'queries', QueryViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('queries/search/', QueryViewSet.as_view({'get': 'search'}), name='query_search'),

]
