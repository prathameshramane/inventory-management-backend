from rest_framework.serializers import ModelSerializer

# Models
from .models import Factory, Product


class FactorySerializer(ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
