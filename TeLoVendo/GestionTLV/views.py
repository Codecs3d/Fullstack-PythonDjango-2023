from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Categoria, Producto, Pedido, Detalle, InfoCliente, Estado
from datetime import datetime
from django.contrib import messages
from .forms import RegisterProduct
from Web.views import get_cant

@login_required(login_url='login')
@user_passes_test(lambda user: user.groups.filter(name='Admin').exists(), redirect_field_name='home')
def ProductView(request):
    productos = Producto.objects.all()
    return render(request, 'core/product.html', {'productos': productos})


@user_passes_test(lambda user: user.groups.filter(name='Admin').exists(), redirect_field_name='home')
@login_required(login_url='login')
def ProductFormView(request, id):
    productos = Producto.objects.all()

    if request.method=="POST":
        producto=Producto()
        messages.success(request, 'Producto creado correctamente')
        if id != 0:
            producto = get_object_or_404(Producto, id_producto = id)
            messages.success(request, 'Producto modificado correctamente')

        producto.nombre = request.POST['nombre']
        producto.descripcion = request.POST['descripcion']
        producto.precio = request.POST['precio']
        producto.stock = request.POST['stock']
        id_categoria = request.POST['categoria']
        producto.imagen = f"img/{id_categoria}.svg"
        producto.sku = datetime.now().strftime("%Y%m%d%H%M%S")
        producto.categoria = get_object_or_404(Categoria, id_categoria = id_categoria)
        producto.save()
        return redirect('product')
    form = RegisterProduct()
    if id != 0:
        producto = get_object_or_404(Producto, id_producto = id)
        form.fields['nombre'].initial = producto.nombre
        form.fields['descripcion'].initial = producto.descripcion
        form.fields['precio'].initial = producto.precio
        form.fields['stock'].initial = producto.stock
        selected = (producto.categoria.id_categoria, producto.categoria.titulo)
        form.fields['categoria'].initial = selected


    return render(request, 'crud/product_form.html', {'form': form, 'productos':productos})



@user_passes_test(lambda user: user.groups.filter(name='Admin').exists(), redirect_field_name='home')
@login_required(login_url='login')
def ProductDeleteView(request, id):
    producto = get_object_or_404(Producto, id_producto = id)
    if request.method=="POST":
        producto.delete()
        messages.success(request, '¡Se ha eliminado!')

        return redirect('product')
    else: 
        return render(request, 'crud/confirmation.html', {'producto': producto})
    


@user_passes_test(lambda user: user.groups.filter(name='Admin').exists(), redirect_field_name='home')
@login_required(login_url='login')
def OrderView(request):
    pedidos = Pedido.objects.all()
    return render(request, 'core/order.html', {'pedidos': pedidos})

@user_passes_test(lambda user: user.groups.filter(name='Admin').exists(), redirect_field_name='home')
@login_required(login_url='login')
def OrderDetailView(request, id):
    pedido = get_object_or_404(Pedido, id_pedido=id)
    detalles = Detalle.objects.filter(id_pedido=id)
    estados = Estado.objects.all()
    subtotal = 0
    for x in detalles:
        print(x.cantidad, x.id_producto.nombre)
        subtotal += x.total
    total = subtotal + 5000
    pedido.total = total
    pedido.subtotal = subtotal
    cliente = get_object_or_404(InfoCliente, id_cliente=pedido.id_cliente.id)
    if request.method=='POST':
        pedido.estado = Estado.objects.get(id_estado=request.POST['estado'])
        pedido.save()
        messages.success(request, '¡Se ha cambiado correctamente!')
        return redirect('order_detail', id=pedido.id_pedido)
    return render(request, 'core/order_detail.html', {'pedido': pedido, 'cliente':cliente, 'estados':estados,'detalles': detalles, 'cant': get_cant(request.session['carrito'])})