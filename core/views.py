from django.shortcuts import get_object_or_404

# Rest Framework
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

# Models
from .models import Factory, Product

# Serializers
from .serializers import FactorySerializer, ProductDetailSerializer, ProductSerializer

# Utils
from .utils import addNewProduct, updateProduct, deleteProduct

# Create your views here.


class FactoryViewSet(ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer


class ProductViewSet(ModelViewSet):
    permission_classes = (AllowAny, )
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, factory_id, *args, **kwargs):
        factory = get_object_or_404(Factory, pk=factory_id)
        product_by_factory = Product.objects.filter(factory=factory)
        return Response(ProductSerializer(product_by_factory, many=True).data)

    def retrieve(self, request, factory_id, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        return Response(ProductDetailSerializer(product).data)

    def create(self, request, factory_id, * args, **kwargs):
        request.data['factory'] = factory_id
        print(addNewProduct(request))
        return super().create(request, *args, **kwargs)

    def update(self, request, pk, *args, **kwargs):
        print(updateProduct(request, pk))
        return super().update(request, *args, **kwargs)

    def destroy(self, request, pk, *args, **kwargs):
        print(deleteProduct(pk))
        return super().destroy(request, *args, **kwargs)
