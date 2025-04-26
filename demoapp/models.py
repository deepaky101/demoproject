from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)