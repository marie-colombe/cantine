from django.db import models




class MenuModel(models.Model):
    dishes = models.OneToOneField('dishes.DishesModel', on_delete=models.CASCADE) 
    create_date = models.DateField(default='2000-01-01')  