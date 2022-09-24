from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Factory(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Factories"

    def __str__(self) -> str:
        return f'{self.name} - {self.location}'


def product_image_directory_path(instance, filename):
    return 'products/{0}/{1}'.format(instance.factory.name, filename)


class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()
    imageUrl = models.ImageField(upload_to=product_image_directory_path)

    # Relations
    factory = models.ForeignKey(to=Factory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} - {self.factory.name}'
