from django.shortcuts import render


def list_dishes(request):
 
   return render(request, 'dishes/plats.html')
