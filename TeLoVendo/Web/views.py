from django.shortcuts import render, get_object_or_404, redirect
from Web.forms import RegisterForm
from Web.data import data
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from GestionTLV.models import Producto, Categoria, InfoCliente, Pedido, Estado, FormaPago, Detalle
from .password_send import send_password
from django.contrib.auth.views import LoginView
from datetime import datetime
from django.contrib import messages

def get_cant(carrito):
    cant = 0
    for x in carrito:
        cant += x["cantidad"]
    return cant

class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    extra_context = {'categorias': Categoria.objects.all(), 'productos': Producto.objects.all()}

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

def HomeView(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    if 'carrito' not in request.session:
        request.session['carrito'] = []
    return render(request, 'core/index.html', {'categorias': categorias, 'productos': productos, 'cant': get_cant(request.session['carrito'])})

def RegisterView(request, id):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    if request.method == "POST":
        user = User()
        group = Group.objects.get(name='Cliente')
        info = InfoCliente()
        if id != 0:
            user = get_object_or_404(User, id=id)
        user.username = request.POST['email']
        user.email = request.POST['email']
        user.first_name = request.POST['f_name']
        user.last_name = request.POST['l_name']
        user.set_password(send_password(request.POST['email']))
        user.save()
        user.groups.add(group)
        info.telefono = request.POST['phone']
        info.region = request.POST['region']
        info.comuna = request.POST[f'comuna-{request.POST["region"]}']
        info.calle = request.POST['street']
        info.numero = request.POST['number']
        info.id_cliente = user
        info.save()
        messages.success(request, 'Usuario creado correctamente')
        return redirect('home')
    chile = data
    form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form, 'chile': chile, 'productos':productos, 'categorias':categorias, 'cant': get_cant(request.session['carrito'])})

@login_required(login_url='login')
def ProfileView(request, id):
    user = get_object_or_404(User, id=id)
    cliente = get_object_or_404(InfoCliente, id_cliente=id)
    pedidos = Pedido.objects.filter(id_cliente=id)
    for x in pedidos:
        x.total = 5000
        x.detalles = Detalle.objects.filter(id_pedido=x.id_pedido)
        for i in x.detalles:
            x.total += i.total
    return render(request, 'registration/profile.html', {'user': user, 'cliente': cliente, 'mispedidos':pedidos,'cant': get_cant(request.session['carrito'])})

@login_required(login_url='login')
def ShoppingView(request):
    if request.method == "POST":
        user = get_object_or_404(User, id=request.user.id)
        carrito = request.session['carrito']
        pedido = Pedido()
        pedido.orden = int(datetime.now().strftime("%Y%m%d%H%M%S"))
        pedido.estado = Estado.objects.get(id_estado=1)
        pedido.id_pago = FormaPago.objects.get(id_pago =request.POST['metodo_pago'])
        pedido.id_cliente = user
        pedido.save()
        
        for x in carrito:
            detalle = Detalle()
            detalle.id_producto = Producto.objects.get(id_producto = x['id'])
            detalle.id_pedido = pedido
            detalle.cantidad = x['cantidad']
            detalle.total = x['cantidad'] * x['precio']
            detalle.save()
        request.session['carrito'] = []
        messages.success(request, 'Pedido realizado correctamente')
        return redirect('shopping')

    return render(request, 'core/shopping.html', {'carrito': request.session["carrito"] , 'cant': get_cant(request.session['carrito']) } )

def AddToCartView(request, id):
    producto = get_object_or_404(Producto, id_producto=id)
    item = {"id":id , "nombre": producto.nombre, "precio": producto.precio, "imagen": producto.imagen, "descripcion":producto.descripcion, "cantidad": 1}
    if "carrito" not in request.session:
        request.session["carrito"] = [item]
    else: 
        var = request.session["carrito"]
        for x in var:
            if x["id"] == id:
                x["cantidad"] += 1
                request.session["carrito"] = var
                return redirect('home')
        var.append(item)
        request.session["carrito"] = var
    messages.success(request, 'Producto agregado al carrito')
    
    return redirect('home')


def RemoveFromCart(request, id):
    var = request.session["carrito"]
    for x in var:
        if x["id"] == id:
            var.remove(x)
            request.session["carrito"] = var
            return redirect('shopping')
    return redirect('shopping')


def OneMoreCart(request, id):
    var = request.session["carrito"]
    for x in var:
        if x["id"] == id:
            x["cantidad"] += 1
            request.session["carrito"] = var
            return redirect('shopping')
    return redirect('shopping')


def OneLessCart(request, id):
    var = request.session["carrito"]
    for x in var:
        print(x["id"])
        if x["id"] == id:
            if x["cantidad"] > 1:
                x["cantidad"] -= 1
                request.session["carrito"] = var
                return redirect('shopping')
            else:
                var.remove(x)
                request.session["carrito"] = var
                return redirect('shopping')
            

