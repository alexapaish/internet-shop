from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()
    image_url = models.CharField(max_length=256)
    emotion = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'