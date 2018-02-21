from django.contrib.auth.views import login
from django.urls import path
from productos import views
from django.contrib.auth import views as auth_views

from productos.views import AboutView

urlpatterns = [
    path('index', views.index, name='index'),
    path('productos', views.catalogo, name='catalogo'),
    path('', views.index, name='index'),
    path('carrito', views.carrito, name='carrito'),
    path('pedir',views.pedir,name='pedir'),
    path('registro',views.register,name='registro'),
    path('login', login, {'template_name':'login.html',}, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('about', AboutView.as_view()),
    path('<categoria>',views.tipo_comida, name='tipo_comida'),
    path('add/<idprod>',views.addpedido, name='añadir pedido'),
    path('delete/<idprod>',views.borrarpedido, name='borrar pedido'),

]