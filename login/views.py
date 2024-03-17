from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required
def base(request):
    return render(request,'base.html')

def inicio(request):
    return render(request,'inicio.html')

def cerrarsesion(request):
    logout(request)
    return redirect('base')

