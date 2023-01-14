from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=150)
    disc=models.TextField(max_length=150,)
    price=models.PositiveIntegerField(default=10)
    picture = models.ImageField(null=True, blank=True, upload_to='images/')

