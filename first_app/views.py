from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def Home(request):
    d = {'author': 'Rahim','age':20,'lst':['python', 'is', 'fun'],'date': datetime.datetime.now()}
    return render(request, 'first_app/home.html',d)









def About(request):
    return render(request, 'first_app/about.html')

def Contact(request):
    return render(request, 'first_app/contact.html')