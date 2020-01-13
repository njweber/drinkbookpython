from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Drink

def home(request):
    drinks = Drink.objects.all()
    return render(request, 'home.html', {'drinks': drinks})

def alldrinks(request):
    drinks = Drink.objects.all()
    return render(request, 'alldrinks.html',  {'drinks': drinks})
    
def partydrinks(request):
    return render(request, 'partydrinks.html')

def findadrink(request):
    return render(request, 'findadrink.html')
	
def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def drink_detail(request, id):
    try:
        drink = Drink.objects.get(id=id)
    except Drink.DoesNotExist:
        raise Http404('Drink Not Found')
    return render(request, 'drink_detail.html', {'drink': drink})
