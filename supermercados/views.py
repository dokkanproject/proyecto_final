from django.template import Template, Context, loader
from django.shortcuts import render, redirect
from supermercados.models import Productos
from supermercados.forms import crearFormulario, buscarFormulario, EditarFormulario

def inicio(request):
    return render(request, 'index.html')

def sobreMi(request):
    return render(request,'about.html')

def agregarProductos(request):
    
    formulario = crearFormulario()
    
    if request.method == 'POST':
        
        formulario = crearFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            prod = Productos(producto=data.get('producto'), marca=data.get('marca') , precio=data.get('precio'), stock=data.get('stock'), fecha=data.get('fecha'))
            prod.save()
            return redirect('buscar_producto')
    
    return render(request, 'add_product.html', {'form':formulario})

def buscarProductos(request):
    
    formulario  = buscarFormulario(request.GET)
    
    if formulario.is_valid():
        producto    = formulario.cleaned_data.get('producto')
        productos   = Productos.objects.filter(producto__icontains=producto)
    else:
        productos   = Productos.objects.all()
    
    return render(request, 'buscar_producto.html', {'productos': productos, 'form': formulario})

def verProducto(request, id):
    producto    = Productos.objects.get(id=id)
    return render(request, 'ver_producto.html',{'producto':producto})

def eliminarProducto(request, id):
    producto    = Productos.objects.get(id=id)
    producto.delete()
    return redirect('buscar_producto')

def editarProducto(request, id):
    prod    = Productos.objects.get(id=id)
    
    formulario = EditarFormulario(initial={'producto': prod.producto, 'marca': prod.marca, 'precio': prod.precio, 'stock': prod.stock, 'fecha': prod.fecha})
    
    
    if request.method == 'POST':
        formulario = EditarFormulario(request.POST)
        
        if formulario.is_valid():
            prod.producto    = formulario.cleaned_data.get('producto')
            prod.precio      = formulario.cleaned_data.get('precio')
            prod.stock       = formulario.cleaned_data.get('stock')
            
            prod.save()
            
            return redirect('buscar_producto')
    
    return render(request, 'editar_producto.html', {'producto':prod, 'form':formulario})
            
            
    
    
    