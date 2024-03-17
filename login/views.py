from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

@login_required
def base(request):
    return render(request,'base.html')

def inicio(request):
    return render(request,'inicio.html')

def cerrarsesion(request):
    logout(request)
    return redirect('base')

def registro_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contraseña = request.POST.get('contraseña')
        # Verificar si el usuario ya existe
        if User.objects.filter(username=usuario).exists():
            messages.error(request, '¡El nombre de usuario ya está en uso! Por favor, elija otro.')
        else:
            # Crear usuario con correo electrónico
            user = User.objects.create_user(username=usuario, password=contraseña)
            user.save()
            messages.success(request, '¡Usuario registrado exitosamente!')
    return render(request, 'registro.html')