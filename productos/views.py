from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import path
from django.views.generic import TemplateView

from productos.models import *
from productos.forms import *
# Create your views here.

def index(request):
    top_productos=Productos.objects.filter(pedidos__id_prod__isnull=False).all().annotate(total=Count('id')).order_by('-total')[:6]
    context={'productos':top_productos}
    return render(request, 'index.html',context)

def catalogo(request):
    lista_productos=Productos.objects.order_by('nombre')
    context={'productos':lista_productos}
    return render(request, 'catalogo.html',context)

def tipo_comida(request, categoria):
    lista_productos=Productos.objects.filter(categoria=categoria)
    context={'productos':lista_productos}
    return render(request, 'catalogo.html',context)

@login_required(login_url='login')
def carrito(request):
    lista_carrito=Productos.objects.filter(carrito__id_prod__isnull=False).filter(carrito__nom_usu=request.user)
    context={'productos':lista_carrito}
    return render(request, 'carrito.html',context)

def addpedido(request, idprod):
    pr=Productos.objects.get(id=idprod)
    c = Carrito(nom_usu=request.user)
    c.save()
    c.id_prod.add(pr)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def borrarpedido(request, idprod):
    Carrito.objects.filter(id_prod=idprod)[0].delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def pedir(request):
    p = Pedidos(nom_usu=request.user)
    p.save()
    c=Productos.objects.filter(carrito__id_prod__isnull=False).filter(carrito__nom_usu=request.user)
    p.id_prod.add(*c)
    lista_carrito=Carrito.objects.filter(nom_usu=request.user).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def register(request):
    if(request.method=='POST'):
        form=UsuarioModelForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            u_usuario=cd['username']
            u_nombre=cd['first_name']
            u_apellido=cd['last_name']
            u_password=cd['password']
            u_email=cd['email']
            usuario=User(username=u_usuario,first_name=u_nombre,last_name=u_apellido,email=u_email)
            usuario.set_password(u_password)
            usuario.save()
            return HttpResponseRedirect("index")
    else:
            form=UsuarioModelForm()
    return render(request,'registro.html',{'form':form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class AboutView(TemplateView):
    template_name = "about.html"