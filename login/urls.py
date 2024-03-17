from django.urls import path
from login.views import base
from login.views import inicio
from login.views import cerrarsesion

urlpatterns = [
    path('',base,name='base'),
    path('inicio/',inicio,name='inicio'),
    path('cerrarsesion/',cerrarsesion,name='cerrarsesion')
    
]
