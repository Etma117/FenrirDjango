from django.shortcuts import render, HttpResponse, redirect
from .models import Productos
from .forms import ProductoForm

# Create your views here.
def home(request):
    return render(request,'catalogos.html')

def productosListar(request):
    productos = (Productos.objects.all())
    data = {'productos' : productos}
    return render (request,'productos.html', data)

def productosCrear(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos/')
    else:
        form= ProductoForm()
        return render (request, 'crear_producto.html', {'form' : form })
    
def productosModificar(request, id):
    producto = Productos.objects.get(id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'crear_producto.html', {'form': form})

def productosEliminar(request, pk):
    producto = Productos.objects.get(pk=pk) 
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')
    
    return render (request, 'eliminar_producto.html', {'producto': producto })  
