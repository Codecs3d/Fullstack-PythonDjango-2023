# Fullstack-PythonDjango-2023
Sitio web demostrativo con aplicaciones web que manipulan datos en una base de datos SQL utilizando Python/Django y las componentes que el lenguaje dispone para su uso; para dar respuesta al requerimiento de finalización del curso "Desarrollo de Aplicaciones Full Stack Python Trainee V2.0", de impartido por "Awakelab-Talento Digital 2023".


Documentación del Proyecto TeLoVendo
TeLoVendo es un sitio de e-commerce desarrollado en Python Django. Proporciona una plataforma para comprar y vender productos en línea. Esta documentación proporciona una descripción general del proyecto, incluyendo su configuración y algunas de las características clave.

Configuración del Proyecto
El proyecto TeLoVendo está configurado utilizando Python Django y cuenta con las siguientes aplicaciones instaladas en el archivo settings.py:

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

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

INSTALLED_APPS: Enumera todas las aplicaciones instaladas en el proyecto, incluyendo Django y las aplicaciones personalizadas GestionTLV y Web.
DATABASES: Configuración de la base de datos PostgreSQL utilizada para el proyecto.
LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL, LOGIN_URL y LOGOUT_URL: Configuración de las URL a las que se redirigirá después de iniciar sesión, cerrar sesión y al intentar acceder a una página restringida sin autenticación.
Funcionalidades Clave
Registro de Usuarios
La aplicación Web del proyecto proporciona un formulario de registro para que los usuarios puedan crear una cuenta. Este formulario está definido en el archivo forms.py.

Autenticación de Usuarios
La autenticación de usuarios se maneja utilizando las funciones proporcionadas por Django. Los usuarios pueden iniciar sesión en la aplicación y cerrar sesión utilizando las vistas y plantillas predeterminadas de Django. La configuración de las URLs de inicio de sesión y cierre de sesión se encuentra en el archivo urls.py.

Modelos de Datos
El proyecto utiliza varios modelos de datos para representar diferentes entidades, como productos, categorías, clientes, pedidos, estados, formas de pago y detalles. Estos modelos se encuentran en la aplicación GestionTLV y están definidos en el archivo models.py.

Vistas
Las vistas del proyecto están definidas en el archivo views.py. Estas vistas controlan la lógica de negocio y renderizan las plantillas correspondientes para mostrar la información en el navegador. Algunas vistas importantes incluyen:

RegisterView: Esta vista maneja el formulario de registro de usuarios.
LoginView: Esta vista maneja el inicio de sesión de usuarios.
Otras vistas relacionadas con la gestión de productos, pedidos, clientes, etc.
Librerías Utilizadas
El proyecto TeLoVendo hace uso de las siguientes librerías y módulos externos:

Django: El framework web utilizado para el desarrollo del proyecto.
psycopg2: El adaptador de base de datos PostgreSQL utilizado para conectarse a la base de datos.
datetime: Un módulo de Python utilizado para trabajar con fechas y tiempos.

Modelos de Datos
El archivo models.py de la aplicación "GestiónTLV" define varios modelos de datos utilizados en el proyecto TeLoVendo. Estos modelos representan entidades clave en el sistema de e-commerce. A continuación, se describen los modelos y sus campos principales:

Modelo Estado
Este modelo representa el estado de un pedido. Tiene los siguientes campos:

id_estado: Un campo de clave primaria para identificar el estado.
titulo: Un campo de texto que indica el título del estado (por ejemplo, "Pendiente", "En Proceso", "En Camino", "Entregado").
Modelo Categoria
Este modelo representa una categoría de productos. Tiene los siguientes campos:

id_categoria: Un campo de clave primaria para identificar la categoría.
titulo: Un campo de texto que indica el título de la categoría.
Modelo FormaPago
Este modelo representa una forma de pago para un pedido. Tiene los siguientes campos:

id_pago: Un campo de clave primaria para identificar la forma de pago.
titulo: Un campo de texto que indica el título de la forma de pago.
Modelo Pedido
Este modelo representa un pedido realizado por un cliente. Tiene los siguientes campos:

id_pedido: Un campo de clave primaria para identificar el pedido.
orden: Un campo entero único que representa el número de orden del pedido.
fecha: Un campo de fecha que almacena la fecha del pedido (por defecto, la fecha actual).
estado: Una relación ForeignKey con el modelo Estado, que indica el estado del pedido.
id_pago: Una relación ForeignKey con el modelo FormaPago, que indica la forma de pago utilizada en el pedido.
id_info: Una relación ForeignKey con el modelo User de Django, que indica la información del cliente que realizó el pedido.
Modelo Producto
Este modelo representa un producto en el catálogo de TeLoVendo. Tiene los siguientes campos:

id_producto: Un campo de clave primaria para identificar el producto.
sku: Un campo de texto que almacena el código SKU del producto.
nombre: Un campo de texto que indica el nombre del producto.
imagen: Un campo de texto que almacena la URL de la imagen del producto (por defecto, se establece una imagen de logo predeterminada).
descripcion: Un campo de texto largo que describe el producto.
precio: Un campo entero que indica el precio del producto.
stock: Un campo entero que indica la cantidad disponible en el stock del producto.
categoria: Una relación ForeignKey con el modelo Categoria, que indica la categoría a la que pertenece el producto.
Modelo Detalle
Este modelo representa un detalle de un pedido, que incluye información sobre un producto específico dentro de un pedido. Tiene los siguientes campos:

id_detalle: Un campo de clave primaria para identificar el detalle.
cantidad: Un campo entero que indica la cantidad del producto en el detalle.
total: Un campo decimal que indica el total del detalle.
id_producto: Una relación ForeignKey con el modelo Producto, que indica el producto relacionado al detalle.
id_pedido: Una relación ForeignKey con el modelo Pedido, que indica el pedido al que pertenece el

Formularios
El archivo forms.py de la aplicación "GestiónTLV" contiene la definición de un formulario utilizado en el proyecto TeLoVendo. Este formulario se utiliza para registrar un nuevo producto y tiene los siguientes campos:

Formulario RegisterProduct
Este formulario permite registrar un nuevo producto en el catálogo de TeLoVendo. Contiene los siguientes campos:

nombre: Un campo de texto para ingresar el nombre del producto.
descripcion: Un campo de texto largo para ingresar la descripción del producto.
precio: Un campo numérico para ingresar el precio del producto.
stock: Un campo numérico para ingresar la cantidad de stock disponible del producto.
categoria: Un campo de selección para elegir la categoría del producto. Las opciones se generan dinámicamente a partir de las categorías existentes en la base de datos.
Además, se aplican algunos atributos HTML y clases CSS a los campos del formulario para mejorar la apariencia y funcionalidad de la interfaz de usuario.

Es importante destacar que este formulario no está vinculado directamente al modelo de datos Producto, sino que se utiliza para recopilar información del usuario y luego procesarla en la lógica de la aplicación para crear un nuevo objeto Producto.

Archivo apps.py
El archivo apps.py de la aplicación "GestiónTLV" contiene la configuración de la aplicación como una instancia de la clase AppConfig. Aquí está el contenido del archivo:

from django.apps import AppConfig

class GestiontlvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'GestionTLV'
En este caso, la clase GestiontlvConfig hereda de AppConfig y define algunas configuraciones para la aplicación, como el campo default_auto_field, que especifica el tipo de campo automático a utilizar para las claves primarias de los modelos.

Archivo admin.py
El archivo admin.py de la aplicación "GestiónTLV" contiene la configuración del panel de administración de Django para los modelos de la aplicación. Aquí tienes el contenido del archivo:

from django.contrib import admin
from .models import Pedido, Producto, Estado, Categoria, FormaPago, Detalle, InfoCliente

# Configuración personalizada para el modelo Pedido en el panel de administración
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'orden', 'fecha', 'estado', 'id_pago')
    list_filter = ('fecha',)
    search_fields = ('orden',)
    list_per_page = 10

admin.site.register(Pedido, PedidoAdmin)

# Configuración personalizada para el modelo Producto en el panel de administración
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'nombre', 'precio', 'stock', 'categoria', 'imagen', 'descripcion')
    list_filter = ('nombre', 'precio', )
    search_fields = ('sku', )

admin.site.register(Producto, ProductoAdmin)

# Configuración personalizada para el modelo Estado en el panel de administración
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', )
    search_fields = ('titulo',)

admin.site.register(Estado, EstadoAdmin)

# Configuración personalizada para el modelo Categoria en el panel de administración
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('titulo', )
    search_fields = ('titulo', )
    list_filter = ('titulo', )

admin.site.register(Categoria, CategoriaAdmin)

# Configuración personalizada para el modelo FormaPago en el panel de administración
class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ('titulo', )
    search_fields = ('titulo', )
    list_filter = ('titulo', )

admin.site.register(FormaPago, FormaPagoAdmin)

# Configuración personalizada para el modelo Detalle en el panel de administración
class DetalleAdmin(admin.ModelAdmin):
    list_display = ('cantidad', 'total', 'id_producto', 'id_pedido')

admin.site.register(Detalle, DetalleAdmin)

# Configuración personalizada para el modelo InfoCliente en el panel de administración
class InfoClienteAdmin(admin.ModelAdmin):
    list_display = ('telefono', 'calle', 'numero', 'comuna', 'region')

admin.site.register(InfoCliente, InfoClienteAdmin)
En este archivo se define la configuración personalizada para cada modelo en el panel de administración de Django. Se utilizan las clases ModelAdmin para especificar cómo se mostrarán y se filtrarán los datos de cada modelo en el panel de administración.
