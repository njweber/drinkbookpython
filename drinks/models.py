from django.db import models

class Drink(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    abv = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True)
    ingredient0 = models.CharField(max_length=100, null=True, blank=True)
    ingredient1 = models.CharField(max_length=100, null=True, blank=True)
    ingredient2 = models.CharField(max_length=100, null=True, blank=True)
    ingredient3 = models.CharField(max_length=100, null=True, blank=True)
    ingredient4 = models.CharField(max_length=100, null=True, blank=True)
    ingredient5 = models.CharField(max_length=100, null=True, blank=True)
    ingredient6 = models.CharField(max_length=100, null=True, blank=True)
    ingredient7 = models.CharField(max_length=100, null=True, blank=True)
