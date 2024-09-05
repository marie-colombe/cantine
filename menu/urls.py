from django.urls import path

from .views import list_menu

app_name='menu'

urlpatterns = [
   path('menu', list_menu, name='menus'),
     
]