from django.conf import settings

# Rest Framework

from rest_framework.serializers import ModelSerializer, SerializerMethodField

# Models
from .models import Factory, Product


class FactorySerializer(ModelSerializer):
    class Meta:
        model = Factory
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    imageUrl = SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_imageUrl(self, instance):
        return settings.HOST_URL+instance.imageUrl.url
