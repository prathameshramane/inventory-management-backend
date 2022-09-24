from django.urls import include, path

# Rest Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import FactoryViewSet, ProductViewSet

factory_router = DefaultRouter()
factory_router.register('', FactoryViewSet, basename='factory-viewset')

product_router = DefaultRouter()
product_router.register('', ProductViewSet, basename='product-viewset')


urlpatterns = [
    path('factories/', include(factory_router.urls)),
    path('factories/<int:factory_id>/products/', include(product_router.urls)),
]
