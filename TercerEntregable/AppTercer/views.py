from django.shortcuts import render
from django.http      import HttpResponse
from .models          import Cliente, Proveedor, Producto, RubroProd, OrdenCompra
from .forms           import AltaCliente, AltaProducto, AltaProveedor, AltaPedido, AltaRubro

# Create your views here.

## -- MENUS -- ##

def inicio(request):
    return render(request, "inicio/inicio.html",)

def clientes(request):
    return render(request, "clientes/inicio.html",)

def proveedores(request):
    return render(request, "proveedores/inicio.html",)

def productos(request):
    return render(request, "productos/inicio.html",)

def rubros(request):
    return render(request, "rubros/inicio.html",)

def pedidos(request):
    return render(request, "pedidos/inicio.html",)

## -- ALTAS -- ##

def AltaClienteForm(request):
    if request.method == 'POST':
        miForm = AltaCliente(request.POST)
        if miForm.is_valid():
            
            info = miForm.cleaned_data
            nuevoCliente = Cliente(nombre=info['nombre'],
                                   apellido=info['apellido'],
                                   fnasc=info['fnasc'],
                                   email=info['email'],
                                   dni=info['dni'],
                                   )
            nuevoCliente.save()
            return render(request, "clientes/inicio.html",{"mensaje": "Nuevo Cliente CREADO Exitosamente"})  
            
        else:
            return render(request, "clientes/inicio.html",{"mensaje": "Formulario Invalido"})  
    
    else:
        miForm = AltaCliente()
    
    return render(request, "clientes/alta.html",{"MiForm": miForm})  

##-------------------------------------------------------------------------------------------
def AltaProveedorForm(request):
    if request.method == 'POST':
        miForm = AltaProveedor(request.POST)
        if miForm.is_valid():
            
            info = miForm.cleaned_data
            nuevoProveedor = Proveedor(nombre=info['nombre'],
                                   contacto=info['contacto'],
                                   email=info['email'],
                                   cuit=info['cuit'],
                                   )
            nuevoProveedor.save()
            return render(request, "proveedores/inicio.html",{"mensaje": "Nuevo Proveedor CREADO Exitosamente"})  
            
        else:
            return render(request, "proveedores/inicio.html",{"mensaje": "Formulario Invalido"})  
    
    else:
        miForm = AltaProveedor()
    
    return render(request, "proveedores/alta.html",{"MiForm": miForm})  

##-------------------------------------------------------------------------------------------
def AltaProductoForm(request):
    if request.method == 'POST':
        miForm = AltaProducto(request.POST)
        if miForm.is_valid():
            
            info = miForm.cleaned_data
            nuevoProducto = Producto(nombre=info['nombre'],
                                   rubro=info['rubro'],
                                   precio=info['precio'],
                                   )
            nuevoProducto.save()
            return render(request, "productos/inicio.html",{"mensaje": "Nuevo Producto CREADO Exitosamente"})  
            
        else:
            return render(request, "productos/inicio.html",{"mensaje": "Formulario Invalido"})  
    
    else:
        miForm = AltaProducto()
    
    return render(request, "productos/alta.html",{"MiForm": miForm})  

##-------------------------------------------------------------------------------------------
def AltaRubroForm(request):
    if request.method == 'POST':
        miForm = AltaRubro(request.POST)
        if miForm.is_valid():
            
            info = miForm.cleaned_data
            nuevoRubro = RubroProd(nombre=info['nombre'],
                                   )
            nuevoRubro.save()
            return render(request, "rubros/inicio.html",{"mensaje": "Nuevo Producto CREADO Exitosamente"})  
            
        else:
            return render(request, "rubros/inicio.html",{"mensaje": "Formulario Invalido"})  
    
    else:
        miForm = AltaRubro()
    
    return render(request, "rubros/alta.html",{"MiForm": miForm})  

##-------------------------------------------------------------------------------------------
def AltaPedidoForm(request):
    if request.method == 'POST':
        miForm = AltaPedido(request.POST)
        if miForm.is_valid():
            
            info = miForm.cleaned_data
            nuevoPedido = OrdenCompra(clientes=info['cliente'],
                                      producto=info['producto'],
                                      cantidad=info['cantidad'],
                                   )
            nuevoPedido.save()
            return render(request, "pedidos/inicio.html",{"mensaje": "Nuevo Pedido CREADO Exitosamente"})  
            
        else:
            return render(request, "pedidos/inicio.html",{"mensaje": "Pedido Invalido"})  
    
    else:
        miForm = AltaPedido()
    
    return render(request, "pedidos/alta.html",{"MiForm": miForm})  





## -- BUSQUEDAS -- ##

## -- LISTADOS -- ##

def lista_clientes(request):
    lista = Cliente.objects.all()
    return render(request, 'l_clientes.html', {'lista_clientes': lista})


