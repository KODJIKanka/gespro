from django.db import models



class Product(models.Model):
    intitule = models.CharField(max_length=100)
    description = models.TextField()
    seller = models.CharField(max_length=100)
    image = models.URLField()
