from django.db import models

class Miembro(models.Model):
    codigo = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.TextField()
    telefono = models.CharField(max_length=255)
    rol = models.CharField(max_length=15)
    imagen = models.ImageField(upload_to='miembro_imagen', null=True, blank=True)
    estado = models.CharField(max_length=20)
    genero = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.codigo}: {self.nombre}"