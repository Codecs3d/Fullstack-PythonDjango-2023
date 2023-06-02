from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from Web.views import HomeView, RegisterView, ProfileView, AddToCartView, ShoppingView, CustomLoginView, OneMoreCart, OneLessCart, RemoveFromCart
from GestionTLV.views import ProductView, OrderView, ProductFormView, ProductDeleteView,OrderDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', CustomLoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name="logout"),
    path('', HomeView, name="home"),
    path('register/<int:id>', RegisterView, name="register"),
    path('telovendo/admin/product', ProductView, name="product"),
    path('telovendo/admin/order', OrderView, name="order"),
    path('telovendo/admin/product/form/<int:id>', ProductFormView, name="product_form"),
    path('telovendo/admin/product/delete/<int:id>', ProductDeleteView, name="product_delete"),
    path('profile/<int:id>', ProfileView, name="profile"),
    path('shopping', ShoppingView, name="shopping"),
    path('product/add/<int:id>', AddToCartView, name="shop_add"),
    path('product/mas/<int:id>', OneMoreCart, name="onemore"),
    path('product/menos/<int:id>', OneLessCart, name="oneless"),
    path('product/delete/<int:id>', RemoveFromCart, name="remove"),
    path('order/detail/<int:id>', OrderDetailView, name="order_detail" )
]
