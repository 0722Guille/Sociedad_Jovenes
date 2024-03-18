from django.urls import path,include
from login.views import base
from login.views import inicio
from login.views import cerrarsesion
from login.views import registro_usuario
from login.views import listaUsuario

urlpatterns = [
    path('',include('miembro.urls')),
    path('',base,name='base'),
    path('inicio/',inicio,name='inicio'),
    path('cerrarsesion/',cerrarsesion,name='cerrarsesion'),
    path('registro_usuario/',registro_usuario,name='registro_usuario'),
    path('listaUsuario/', listaUsuario, name='listaUsuario')
]
