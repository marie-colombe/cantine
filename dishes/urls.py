from django.urls import path

from .views import list_dishes

app_name='dishes'

urlpatterns = [
   path('dishes', list_dishes, name='dishe'),
     
]