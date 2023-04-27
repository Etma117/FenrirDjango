from django.shortcuts import render, HttpResponse
from . models import Laptops

# Create your views here.
def hello(request):
    return HttpResponse('hola')

def laptopsListar(request):
    laps = Laptops.objects.all()
    data = {'laps' : laps}
    return render (request,'laptops.html', data)
