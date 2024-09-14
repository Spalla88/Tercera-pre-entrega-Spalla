from django.db import models
from django.contrib.auth.models import User

class MaquinaAgricola(models.Model):
    Maquina_Seleccion = [
        ('Tractores', 'Tractores'),
        ('Cosechadoras', 'Cosechadoras'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.CharField(max_length=200)
    maquina = models.CharField(max_length=15, choices=Maquina_Seleccion, default='Tractores')
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    descripcion = models.TextField(null=True, blank=True)
    year = models.IntegerField() 
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fechaPublicacion = models.DateTimeField(auto_now_add=True)
    telefonoContacto = models.IntegerField()
    emailContacto = models.EmailField()
    imagenMaquina = models.ImageField(null=True, blank=True, upload_to="imagenes/")

    class Meta:
        ordering = ['usuario', '-fechaPublicacion']

    def __str__(self):
        return self.titulo    

class Comentario(models.Model):
    comentario = models.ForeignKey(MaquinaAgricola, related_name='comentarios', on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40)
    mensaje = models.TextField(null=True, blank=True)
    fechaComentario = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fechaComentario']

    def __str__(self):
        return '%s - %s' % (self.nombre, self.comentario)
    

# class Cliente(models.Model):
#     nombre_completo = models.CharField(max_length=100)
#     cuit = models.CharField(max_length=11)
#     email = models.EmailField()
#     telefono = models.CharField(max_length=15)
#     localidad = models.CharField(max_length=100)

#     def __str__(self):
#         return self.nombre_completo

# class Tractor(models.Model):
#     familia = models.CharField(max_length=100)
#     modelo = models.CharField(max_length=100)
#     serie = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.familia} {self.modelo}"

# class Cosechadora(models.Model):
#     familia = models.CharField(max_length=100)
#     modelo = models.CharField(max_length=100)
#     serie = models.CharField(max_length=100)

#     def __str__(self):
#         return f"{self.familia} {self.modelo}"