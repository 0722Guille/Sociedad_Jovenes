from django.shortcuts import render,redirect
from datetime import datetime
from .models import Miembro
# from django.db.models.functions import Coalesce
from django.contrib import messages



# Create your views here.

def miembro(request):
    miembros=Miembro.objects.all()
    count= miembros.count()
    return render(request,'miembro.html',{'miembros': miembros})



def agregarMiembro(request):
    
    nombre= request.POST['nombre']
    apellido= request.POST['apellido']
    direccion= request.POST['direccion']
    rol= request.POST['rol']
    telefono= request.POST['telefono']
    imagen = request.FILES.get('imagen')  # Aquí es request.FILES en lugar de request.FILE
    estado=request.POST['estado']
    genero=request.POST['genero']
    fecha_nacimiento= request.POST.get('fecha_nacimiento')
    fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y-%m-%d').date() if fecha_nacimiento else None
    
    
    miembro=Miembro.objects.create(
        
        nombre=nombre,
        apellido=apellido,
        direccion=direccion,
        rol=rol,
        telefono=telefono,
        imagen=imagen,
        estado=estado,
        genero=genero,
        fecha_nacimiento= fecha_nacimiento
        
    )
    
    
    messages.success(request, 'Miembro agreagado exitosamente.')
    
    return redirect('miembro')

def eliminarMiembro(request,codigo):
    miembro= Miembro.objects.get(codigo=codigo)
    miembro.delete()
    return redirect('miembro')

def detalleMiembro(request):
    miembros= Miembro.objects.all()
    total_miembros = miembros.count() 
    
    
    total_masculino= miembros.filter(genero='Masculino').count()
    total_femenino= miembros.filter(genero='Femenino').count()
    
    
    total_activo= miembros.filter(estado='Activo').count()
    total_inactivo= miembros.filter(estado='Inactivo').count()
    
    return render(request, 'detallemiembro.html', {
        'miembros': miembros,
        'total_miembros': total_miembros,  # Corregido de tota_miembros a total_miembros
        'total_masculino': total_masculino,
        'total_femenino': total_femenino,
        'total_activo': total_activo,
        'total_inactivo': total_inactivo
    })
