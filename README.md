# Fullstack-PythonDjango-2023
**Sitio demostrativo con aplicaciones web** que manipulan datos en una base de datos SQL utilizando **Python/Django** y las componentes que el lenguaje dispone para su uso; para dar respuesta al requerimiento de finalización del curso **"Desarrollo de Aplicaciones Full Stack Python Trainee V2.0"** , impartido por **"Awakelab-Talento Digital 2023"**.


# Documentación del Proyecto TeLoVendo
![TeloVendo](https://github.com/Codecs3d/Fullstack-PythonDjango-2023/assets/123422865/7cdcc708-6c64-4292-a724-2cb0453b5dc2)


**TeLoVendo es un sitio de e-commerce desarrollado en Python Django**. Proporciona una plataforma para comprar y vender productos en línea. Esta documentación proporciona una descripción general del proyecto, incluyendo su configuración y algunas de las características clave.

Desarrollado por:

- Christian Torres
- Madeleine Gallardo
- Paulette Diemer
- Dann Espinoza

# Información General TeloVendo

TeloVendo es un proyecto de comercio electrónico desarrollado en Django.
Perfil de prueba:
- **Username:** asistencia.telovendo@gmail.com
- **Password:** admin12345!

## Descripción

El proyecto **TeloVendo** consiste en una plataforma de venta en línea que permite a los usuarios explorar y comprar productos de diversas categorías. La aplicación consta de dos partes principales: la aplicación **"Web"** que se encarga de la interfaz de usuario y la interacción con los clientes, y la aplicación **"GestionTLV"** que se encarga de la gestión interna de los productos, pedidos y clientes.

## Características

- Registro y autenticación de usuarios.
- Búsqueda y filtrado de productos por categoría.
- Agregar productos al carrito de compras.
- Realizar pedidos y gestionar el estado de los mismos.
- Administración de productos, categorías y clientes en el panel de administración.
- Envío de contraseñas por correo electrónico al registrarse.

## Tecnologías y Librerías utilizadas

- Django: Framework de desarrollo web utilizado para la implementación del proyecto.
    - datetime: Un módulo de Python utilizado para trabajar con fechas y tiempos.
- Python: Lenguaje de programación utilizado en el backend.
- HTML, CSS y JavaScript: Tecnologías como Grid.Js que facilita el uso de tablas dinámicas en el frontend para la creación de la interfaz de usuario.
- Bootstrap: Framework de CSS utilizado para el diseño y la responsividad del sitio.
    - LordIcon.
    - Bootstrap Icon.   
- PostgreSQL: Sistema de gestión de bases de datos utilizado para almacenar los datos del proyecto.
    - psycopg2: El adaptador de base de datos **PostgreSQL** utilizado para conectarse a la base de datos.


## Estructura del Proyecto

El proyecto se organiza en las siguientes aplicaciones:

### Aplicación "Web"

- **models.py**: Define los modelos de datos utilizados en la aplicación "Web", incluyendo el registro de usuarios, información de clientes y pedidos.
- **forms.py**: Contiene los formularios utilizados para el registro y el inicio de sesión de los usuarios.
- **views.py**: Contiene las vistas y lógica de negocio de la aplicación "Web", incluyendo las vistas para la página de inicio, registro, perfil de usuario y proceso de compra.
- **password.py**: Contiene funciones para generar contraseñas aleatorias y enviarlas por correo electrónico.

### Aplicación "GestionTLV"

- **models.py**: Define los modelos de datos utilizados en la aplicación "GestionTLV", incluyendo productos, categorías, pedidos y detalles.
- **forms.py**: Contiene los formularios utilizados para el registro de productos.
- **admin.py**: Registra los modelos en el panel de administración de Django y configura las opciones de visualización.
- **views.py**: Contiene las vistas y lógica de negocio de la aplicación "GestionTLV", incluyendo vistas para administrar pedidos y productos.

## Configuración y Ejecución

A continuación se detallan los pasos para configurar y ejecutar el proyecto:

1. Clona el repositorio de GitHub: `git clone https://github.com/tu_usuario/telovendo.git`.
2. Crea un entorno virtual e instala las dependencias del proyecto: `pip install -r requirements.txt`.
3. Configura la conexión a la base de datos en el archivo `settings.py`.
4. Aplica la migración inicial a la base de datos: `python manage.py makemigrations`.
5. Realiza las migraciones de la base de datos: `python manage.py migrate`.
6. Crea un superusuario: `python manage.py createsuperuser`.
7. Inicia el servidor de desarrollo: `python manage.py runserver`.
8. Accede al panel de administración: Abre `http://localhost:8000/admin` en tu navegador.
9. Explora la aplicación web: Visita `http://localhost:8000` en tu navegador.

## Contribución

Si deseas contribuir al proyecto TeloVendo, sigue estos pasos:

1. Realiza un fork del repositorio en GitHub.
2. Clona tu fork del repositorio en tu máquina local.
3. Crea una rama para tu contribución: `git checkout -b mi-contribucion`.
4. Realiza los cambios y mejoras necesarias en tu rama local.
5. Realiza commits de tus cambios: `git commit -m "Mi contribución"`.
6. Sube tus cambios a tu repositorio en GitHub: `git push origin mi-contribucion`.
7. Crea una Pull Request en el repositorio original para revisar tus cambios.

## Mejoras potenciales

A continuación se presentan algunas mejoras que se podrían implementar en el sistema de e-commerce:

1. Integración con redes sociales: Permitir a los usuarios compartir productos y promociones en sus perfiles de redes sociales, lo que puede ayudar a aumentar la visibilidad y atraer a nuevos clientes.

2. Mejoras en la interfaz de usuario: Evaluar la usabilidad y el diseño de la interfaz de usuario para garantizar una experiencia fluida y atractiva. Considera mejorar la navegación, la disposición de los elementos y la capacidad de respuesta en dispositivos móviles.

3. Optimización de rendimiento: Realizar mejoras en el rendimiento del sistema, como la optimización de consultas a la base de datos, el almacenamiento en caché de datos frecuentemente utilizados y la reducción del tiempo de carga de páginas.

4. Incorporación de análisis y métricas: Implementar herramientas de análisis para recopilar datos sobre el comportamiento de los usuarios, las conversiones de ventas y otros indicadores clave. Esto te ayudará a comprender mejor el rendimiento del sistema y tomar decisiones informadas para mejorarlo continuamente.

## Contacto

Si tienes alguna pregunta, sugerencia o problema relacionado con el proyecto TeloVendo, no dudes en ponerte en contacto con nosotros. Puedes enviarnos un correo electrónico a [asistencia.telovendo@gmail.com](mailto:asistencia.telovendo@gmail.com) o abrir un problema en GitHub.

Estaremos encantados de ayudarte y recibir tus comentarios para mejorar continuamente el proyecto.
¡Gracias por tu interés en TeloVendo! Esperamos que disfrutes utilizando nuestra plataforma de e-commerce. Siempre estamos abiertos a nuevas ideas y contribuciones. ¡Bienvenido a nuestra comunidad!

# Revisión exhaustiva del Proyecto TeLoVendo
El proyecto **TeLoVendo** está configurado utilizando **Python Django** y cuenta con las siguientes aplicaciones instaladas en el archivo **settings.py**:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'GestionTLV',
    'Web'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'telovendo',
        'USER': 'admin',
        'PASSWORD':'123',
        'HOST':'localhost',
        'PORT':'',
    }
}

#Esta es la configuración por defecto de nuestra BBDD, tu puedes
#hacer la modificación que estimes, antes de efectuar el comando makemigrations.

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
```

 
- **INSTALLED**_**APPS** : Enumera todas las aplicaciones instaladas en el proyecto, incluyendo Django y las aplicaciones personalizadas GestionTLV y Web.<br> 
- **DATABASES** : Configuración de la base de datos **PostgreSQL** utilizada para el proyecto.<br> 
- **LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL, LOGIN_URL y LOGOUT_URL** : Configuración de las URL a las que se redirigirá después de iniciar sesión, cerrar sesión y al intentar acceder a una página restringida sin autenticación.<br>


# Funcionalidades Clave: GestionTLV

## Registro de Usuarios
La aplicación Web del proyecto proporciona un **formulario de registro** para que los usuarios puedan crear una cuenta. Este formulario está definido en el archivo **forms.py**.<br> 

![registro](https://github.com/Codecs3d/Fullstack-PythonDjango-2023/assets/123422865/682734cc-233c-4dcf-b958-ab6e69c6ab0c)

## Autenticación de Usuarios
La **autenticación de usuarios** se maneja utilizando las **funciones proporcionadas por Django** . Los usuarios pueden iniciar sesión en la aplicación y cerrar sesión utilizando las vistas y plantillas predeterminadas de Django. La **configuración de las URLs** de inicio de sesión y cierre de sesión se encuentra en el archivo **urls.py**.

![sesión](https://github.com/Codecs3d/Fullstack-PythonDjango-2023/assets/123422865/45967745-79dd-47ed-af2b-f017de0cd7bf)

## Modelos de Datos
El proyecto utiliza varios **modelos** de datos para representar diferentes entidades, como **productos, categorías, clientes, pedidos, estados, formas de pago y detalles**. Estos modelos se encuentran en la aplicación **GestionTLV** y están definidos en el archivo **models.py**.

## Vistas
Las **vistas del proyecto** están definidas en el archivo **views.py**. Estas vistas controlan la **lógica de negocio y renderizan las plantillas** correspondientes para mostrar la información en el navegador. Algunas vistas importantes incluyen:

- **RegisterView:** Esta vista maneja el formulario de registro de usuarios.</br>
- **LoginView:** Esta vista maneja el inicio de sesión de usuarios.</br>

También se cuenta con otras vistas relacionadas con la gestión de productos, pedidos, clientes, etc.

# Modelos de Datos

El archivo **models.py** de la aplicación **"GestiónTLV"** define varios modelos de datos utilizados en el proyecto **TeLoVendo**. Estos modelos representan entidades clave en el sistema de e-commerce. A continuación, se describen los modelos y sus campos principales:

### Modelo Estado
Este modelo representa el estado de un pedido. Tiene los siguientes campos:

- **id_estado:** Un campo de clave primaria para identificar el estado.</br>
- **titulo:** Un campo de texto que indica el título del estado (por ejemplo, "Pendiente", "En Proceso", "En Camino", "Entregado").</br>

### Modelo Categoria
Este modelo representa una categoría de productos. Tiene los siguientes campos:

- **id_categoria:** Un campo de clave primaria para identificar la categoría.</br>
- **titulo:** Un campo de texto que indica el título de la categoría.</br>

### Modelo FormaPago
Este modelo representa una forma de pago para un pedido. Tiene los siguientes campos:

- **id_pago:** Un campo de clave primaria para identificar la forma de pago.</br>
- **titulo:** Un campo de texto que indica el título de la forma de pago.</br>

### Modelo Pedido
Este modelo representa un pedido realizado por un cliente. Tiene los siguientes campos:

- **id_pedido:** Un campo de clave primaria para identificar el pedido.</br>
- **orden:** Un campo entero único que representa el número de orden del pedido.</br>
- **fecha:** Un campo de fecha que almacena la fecha del pedido (por defecto, la fecha actual).</br>
- **estado:** Una relación ForeignKey con el modelo Estado, que indica el estado del pedido.</br>
- **id_pago:** Una relación ForeignKey con el modelo FormaPago, que indica la forma de pago utilizada en el pedido.</br>
- **id_info:** Una relación ForeignKey con el modelo User de Django, que indica la información del cliente que realizó el pedido.</br>


### Modelo Producto
Este modelo representa un producto en el catálogo de **TeLoVendo**. Tiene los siguientes campos:

- **id_producto:** Un campo de clave primaria para identificar el producto.</br>
- **sku:** Un campo de texto que almacena el código SKU del producto.</br>
- **nombre:** Un campo de texto que indica el nombre del producto.</br>
- **imagen:** Un campo de texto que almacena la URL de la imagen del producto (por defecto, se establece una imagen de logo predeterminada).</br>
- **descripcion:** Un campo de texto largo que describe el producto.</br>
- **precio:** Un campo entero que indica el precio del producto.</br>
- **stock:** Un campo entero que indica la cantidad disponible en el stock del producto.</br>
- **categoria:** Una relación ForeignKey con el modelo Categoria, que indica la categoría a la que pertenece el producto.</br>

![computacion](https://github.com/Codecs3d/Fullstack-PythonDjango-2023/assets/123422865/e97df2c6-7afc-4168-8259-40dac74075db)

### Modelo Detalle
Este modelo representa un detalle de un pedido, que incluye información sobre un producto específico dentro de un pedido. Tiene los siguientes campos:

- **id_detalle:** Un campo de clave primaria para identificar el detalle.</br>
- **cantidad:** Un campo entero que indica la cantidad del producto en el detalle.</br>
- **total:** Un campo decimal que indica el total del detalle.</br>
- **id_producto:** Una relación ForeignKey con el modelo Producto, que indica el producto relacionado al detalle.</br>
- **id_pedido:** Una relación ForeignKey con el modelo Pedido, que indica el pedido al que pertenece el detalle.</br>

Este modelo permite almacenar la **información detallada** de los productos incluidos en un pedido, como la cantidad, el total y las referencias a los modelos **Producto y Pedido**. Esto proporciona una estructura para realizar un seguimiento de los productos específicos asociados a cada pedido.

![carro](https://github.com/Codecs3d/Fullstack-PythonDjango-2023/assets/123422865/6c1b2793-643e-49b6-9b78-78465d3ab66a)


# Formularios GestiónTLV
El archivo **forms.py** de la aplicación **"GestiónTLV"** contiene la definición de un formulario utilizado en el proyecto **TeLoVendo**.

### Formulario RegisterProduct
Este formulario permite registrar un nuevo producto en el catálogo de TeLoVendo. Contiene los siguientes campos:

- **nombre:** Un campo de texto para ingresar el nombre del producto.</br>
- **descripcion:** Un campo de texto largo para ingresar la descripción del producto.</br>
- **precio:** Un campo numérico para ingresar el precio del producto.</br>
- **stock:** Un campo numérico para ingresar la cantidad de stock disponible del producto.</br>
- **categoria:** Un campo de selección para elegir la categoría del producto. Las opciones se generan dinámicamente a partir de las categorías existentes en la base de datos.</br>

Además, se aplican algunos atributos **HTML y clases CSS** a los campos del formulario **para mejorar la apariencia y funcionalidad de la interfaz de usuario**.

Es importante destacar que **este formulario no está vinculado directamente al modelo de datos Producto** , sino que **se utiliza para recopilar información del usuario** y luego procesarla en la lógica de la aplicación **para crear un nuevo objeto Producto**.

# Archivo apps.py
El archivo **apps.py** de la aplicación **"GestiónTLV"** contiene la configuración de la aplicación como **una instancia de la clase AppConfig** . Aquí está el contenido del archivo:

```python
from django.apps import AppConfig

class GestiontlvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GestionTLV'
```
En este caso, la clase **GestiontlvConfig** hereda de **AppConfig** y define algunas configuraciones para la aplicación, como el campo **default_auto_field**, que especifica el tipo de campo automático a utilizar para las claves primarias de los modelos.

# Archivo admin.py
El archivo **admin.py** de la aplicación **"GestiónTLV"** contiene la configuración del panel de administración de Django para los modelos de la aplicación. Aquí tienes el contenido del archivo:

```python
from django.contrib import admin
from .models import Pedido, Producto, Estado, Categoria, FormaPago, Detalle, InfoCliente

#Configuración personalizada para el modelo Pedido en el panel de administración
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'orden', 'fecha', 'estado', 'id_pago')
    list_filter = ('fecha',)
    search_fields = ('orden',)
    list_per_page = 10

admin.site.register(Pedido, PedidoAdmin)

#Configuración personalizada para el modelo Producto en el panel de administración
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'nombre', 'precio', 'stock', 'categoria', 'imagen', 'descripcion')
    list_filter = ('nombre', 'precio', )
    search_fields = ('sku', )

admin.site.register(Producto, ProductoAdmin)

#Configuración personalizada para el modelo Estado en el panel de administración
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', )
    search_fields = ('titulo',)

admin.site.register(Estado, EstadoAdmin)

#Configuración personalizada para el modelo Categoria en el panel de administración
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', )
    search_fields = ('titulo', )
    list_filter = ('titulo', )

admin.site.register(Categoria, CategoriaAdmin)

#Configuración personalizada para el modelo FormaPago en el panel de administración
class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ('titulo', )
    search_fields = ('titulo', )
    list_filter = ('titulo', )

admin.site.register(FormaPago, FormaPagoAdmin)

#Configuración personalizada para el modelo Detalle en el panel de administración
class DetalleAdmin(admin.ModelAdmin):
    list_display = ('cantidad', 'total', 'id_producto', 'id_pedido')

admin.site.register(Detalle, DetalleAdmin)

#Configuración personalizada para el modelo InfoCliente en el panel de administración
class InfoClienteAdmin(admin.ModelAdmin):
    list_display = ('telefono', 'calle', 'numero', 'comuna', 'region')

admin.site.register(InfoCliente, InfoClienteAdmin)
```

En este archivo se define la **configuración personalizada** para cada modelo en el panel de administración de Django. Se utilizan las **clases ModelAdmin** para especificar cómo se mostrarán y se filtrarán los datos de cada modelo en el panel de administración.

# Formularios Web

## Archivo forms.py:

```python
from django import forms
from Web.data import regiones
class RegisterForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico', max_length=100, widget=forms.EmailInput(attrs={'class':'w-100'}))
    f_name = forms.CharField(label='Nombre', max_length=100, widget=forms.TextInput(attrs={'class':'w-100'}))
    l_name = forms.CharField(label='Apellido', max_length=100, widget=forms.TextInput(attrs={'class':'w-100'}))
    phone = forms.CharField(label='Celular', max_length=9, widget=forms.NumberInput(attrs={'class':'w-100'}))
    street = forms.CharField(label='Calle', max_length=100, widget=forms.TextInput(attrs={'class':'w-100'}))
    number = forms.CharField(label='Número', max_length=100, widget=forms.NumberInput(attrs={'class':'w-100'}))
    region = forms.ChoiceField(choices=regiones, label='Región', widget=forms.Select(attrs={'class':'w-100'}))
    fecha_nac = forms.DateField(label='Fecha de nacimiento', widget=forms.DateInput(attrs={'type': 'date', 'class':'form-control'}))


class LoginForm(forms.Form):
    email = forms.EmailField(label='Correo electrónico', max_length=100)
    password = forms.CharField(label='Contraseña', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
```

- **RegisterForm:** Este formulario se utiliza para capturar la información de registro de un usuario en el sitio web. Contiene campos como el correo electrónico, nombre, apellido, celular, dirección, región y fecha de nacimiento.</br>

- **LoginForm:** Este formulario se utiliza para capturar las credenciales de inicio de sesión de un usuario. Contiene campos para el correo electrónico y la contraseña.</br>

Ambos formularios están definidos en el archivo forms.py de la aplicación "Web". Estos formularios se utilizan para validar y procesar los datos ingresados por los usuarios durante el registro y el inicio de sesión.

## Archivo password_send.py:

```python
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string

def get_password():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(15))
    return contrasena



def send_password(email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    server = smtplib.SMTP(smtp_server, smtp_port)

    server.starttls()
    server.login('asistencia.telovendo@gmail.com', 'shxbgahubinfkhek')
    password = get_password()
    html = f"""
    <h2 style="color:#a5e830">Contraseña:</h2>
    <label style="color:red">{password}</label>
    """
    msg = MIMEMultipart()

    msg['From'] = 'asistencia.telovendo@gmail.com'
    msg['To'] = email
    msg['Subject'] = 'Envío de Contraseña'
    content = MIMEText(html, 'html')
    msg.attach(content)
    server.send_message(msg)

    server.quit()
    return password
```

- **get_password():** Esta función genera una contraseña aleatoria de 15 caracteres que incluye letras mayúsculas, letras minúsculas, dígitos y caracteres especiales.</br>

- **send_password(email):** Esta función envía un correo electrónico a la dirección proporcionada con la contraseña generada anteriormente. Se utiliza para enviar la contraseña a los usuarios que la han olvidado.</br>

Esta lógica relacionada con el envío de contraseñas se encuentra en el archivo password_send.py. Se utiliza el servidor SMTP de Gmail para enviar los correos electrónicos y se establece una conexión segura utilizando el puerto 587.

# Funcionalidades Clave aplicación : Web

## Vistas en la aplicación "Web". 

```python
def get_cant(carrito):
    cant = 0
    for x in carrito:
        cant += x["cantidad"]
    return cant

class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    extra_context = {'categorias': Categoria.objects.all(), 'productos': Producto.objects.all()}
 ```
   
- **CustomLoginView:** Esta clase es una vista personalizada para el inicio de sesión. Hereda de LoginView proporcionada por Django y realiza algunas modificaciones. Establece el atributo redirect_authenticated_user en True para redirigir a los usuarios autenticados a la página principal. Además, define el atributo extra_context para pasar las categorías y productos a la plantilla de inicio de sesión.

 

```python 
def HomeView(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    if 'carrito' not in request.session:
        request.session['carrito'] = []
    return render(request, 'core/index.html', {'categorias': categorias, 'productos': productos, 'cant': get_cant(request.session['carrito'])})
 ```
    
- **HomeView:** Esta vista es la página principal del sitio web. Obtiene todas las categorías y productos de la base de datos y renderiza la plantilla core/index.html. También verifica si el carrito de compras está almacenado en la sesión del usuario y, de lo contrario, lo inicializa.

```python 
def RegisterView(request, id):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    if request.method == "POST":
        user = User()
        group = Group.objects.get(name='Cliente')
        info = InfoCliente()
        if id != 0:
            user = get_object_or_404(User, id=id)
            cliente = get_object_or_404(InfoCliente, id_cliente=id)
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
        return redirect('login')
    chile = data
    form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form, 'chile': chile, 'productos':productos, 'categorias':categorias, 'cant': get_cant(request.session['carrito'])})
```    
    
- **RegisterView:** Esta vista se utiliza para el registro de nuevos usuarios. Si se recibe una solicitud POST, se crea un nuevo usuario en la base de datos utilizando los datos proporcionados en el formulario RegisterForm. Además, se crea una instancia del modelo InfoCliente para almacenar la información adicional del cliente. Si el registro es exitoso, se redirige al usuario a la página de inicio de sesión.


```python 
@login_required(login_url='login')
def ProfileView(request, id):
    user = get_object_or_404(User, id=id)
    cliente = get_object_or_404(InfoCliente, id_cliente=id)
    return render(request, 'registration/profile.html', {'user': user, 'cliente': cliente, 'cant': get_cant(request.session['carrito'])})
 ```
    
- **ProfileView:** Esta vista muestra el perfil de un usuario registrado. Obtiene el objeto User y InfoCliente correspondientes al ID proporcionado y los pasa a la plantilla registration/profile.html.

```python 
def OrderDetailView(request, id):
    pedido = get_object_or_404(Pedido, id_pedido=id)
    detalles = Detalle.objects.filter(id_pedido=id)
    return render(request, 'core/order_detail.html', {'pedido': pedido, 'detalles': detalles, 'cant': get_cant(request.session['carrito'])})
```

- **OrderDetailView:** Esta vista muestra los detalles de un pedido específico. Obtiene el objeto Pedido y los detalles relacionados utilizando el ID proporcionado y los pasa a la plantilla core/order_detail.html.


```python
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

        return redirect('shopping')

    return render(request, 'core/shopping.html', {'carrito': request.session["carrito"] , 'cant': get_cant(request.session['carrito']) } )
 ```
 
- **ShoppingView:** Esta vista maneja la funcionalidad de compra. Si se recibe una solicitud POST, se crea un nuevo objeto Pedido en la base de datos con los detalles del carrito de compras del usuario. Luego, se crean objetos Detalle relacionados con el pedido para cada producto en el carrito. Finalmente, se redirige al usuario a la página de compras.


```python
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
    return redirect('home')
```    

- **AddToCartView:** Esta vista se utiliza para agregar un producto al carrito de compras. Obtiene el objeto Producto correspondiente al ID proporcionado y agrega un diccionario que representa el producto al carrito de compras almacenado en la sesión del usuario.

```python
def RemoveFromCart(request, id):
    var = request.session["carrito"]
    for x in var:
        if x["id"] == id:
            var.remove(x)
            request.session["carrito"] = var
            return redirect('shopping')
    return redirect('shopping')
```
- **RemoveFromCart:** Esta vista se utiliza para eliminar un producto del carrito de compras. Busca el producto correspondiente al ID proporcionado y lo elimina del carrito almacenado en la sesión del usuario.

```python
def OneMoreCart(request, id):
    var = request.session["carrito"]
    for x in var:
        if x["id"] == id:
            x["cantidad"] += 1
            request.session["carrito"] = var
            return redirect('shopping')
    return redirect('shopping')
```

- **OneMoreCart:** Esta vista se utiliza para aumentar la cantidad de un producto en el carrito de compras. Busca el producto correspondiente al ID proporcionado y aumenta su cantidad en 1 en el carrito almacenado en la sesión del usuario.

```python
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
 ```        
        
- **OneLessCart:** Esta vista se utiliza para disminuir la cantidad de un producto en el carrito de compras. Busca el producto correspondiente al ID proporcionado y disminuye su cantidad en 1 en el carrito almacenado en la sesión del usuario. Si la cantidad llega a 0, el producto se elimina del carrito.

# Tablas dinámicas con JavaScript

```js
function createtable(data) {
    new gridjs.Grid({
        columns: ["SKU", "NOMBRE", "PRECIO", "CANTIDAD"],
        data: data,
        search: true,
        sort: true
    }).render(document.getElementById("wrapper"));
}
```

El **archivo table.js** en la carpeta static del proyecto "Web" contiene una función llamada **createtable(data)**. Esta función utiliza la biblioteca **gridjs** para crear una tabla dinámica en la página web.

La tabla tendrá cuatro columnas: **"SKU", "NOMBRE", "PRECIO" y "CANTIDAD"**. Los datos de la tabla se pasan como argumento a la función createtable(data). La variable data debe contener los datos en un formato adecuado para la biblioteca gridjs.

La tabla creada tendrá funcionalidades de **búsqueda y ordenamiento**, ya que se establecen las opciones **search: true y sort: true** en la configuración de la tabla.


# Conclusión y agradecimiento

Todo proyecto puede seguir mejorandose de forma indefinida, hasta acá hemos llegado nosotros y nosotras...¿hasta dónde llegarás tú?.

- **¿Quieres ser nuestro cliente?**
Si necesitas este sistema y quieres modificaciones especificas para cubrir las necesidades de tu empresa, contactanos, para que podamos agendar una reunión.

- **¿Eres desarrollad@r?**
Agradecemos tu interés en la documentación del proyecto "TeLoVendo". Esperamos que esta información te sea útil y te brinde una comprensión sólida del sistema de e-commerce desarrollado con Django.

Si tienes alguna pregunta adicional o necesitas más información, no dudes en contactarnos. ¡Gracias por tu atención y apoyo!

Atentamente,  
El equipo de desarrollo de TeLoVendo<br> 
**[asistencia.telovendo@gmail.com](mailto:asistencia.telovendo@gmail.com)**
