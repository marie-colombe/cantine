from django.db import models




class DishesModel(models.Model):
    name = models.CharField(max_length=30)
    summary = models.CharField(max_length=30)