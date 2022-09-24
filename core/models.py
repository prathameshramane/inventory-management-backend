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


class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    description = models.TextField()

    # Relations
    factory = models.ForeignKey(to=Factory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.name} - {self.factory.name}'
