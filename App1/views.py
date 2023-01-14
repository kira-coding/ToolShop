from django.shortcuts import render
from .models import *
# Create your views here.


def home(response):
    p = Product.objects.all()
    
    return render(response, 'App1/home.html', {'k': p})

