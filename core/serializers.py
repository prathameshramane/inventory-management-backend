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
        fields = ('id', 'factory', 'name', 'quantity',
                  'description', 'imageUrl', 'image')
        extra_kwargs = {
            'image': {
                'write_only': True
            },
            'factory': {
                'write_only': True
            },
            'imageUrl': {
                'read_only': True
            }
        }

    def get_imageUrl(self, instance):
        return settings.HOST_URL+instance.image.url
