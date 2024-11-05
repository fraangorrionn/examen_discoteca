from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(default='default@example.com')
    direccion = models.CharField(max_length=255, default='sin_direccion')
    copas_favoritas = models.ManyToManyField('Copa', through='Favoritas', related_name='clientes_favoritos')

class Copa(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)
    
class Favoritas(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    copa = models.ForeignKey(Copa, on_delete=models.CASCADE)
    fecha_agregado = models.DateField(auto_now_add=True)
    prioridad = models.IntegerField(default=1)
    notas = models.TextField(blank=True)

class Voto(models.Model):
   cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
   copa = models.ForeignKey(Copa, on_delete=models.CASCADE, related_name='votos')
   puntuacion = models.IntegerField()
   comentario = models.TextField(blank=True)
   fecha_hora = models.DateTimeField(default=timezone.now)

   class Meta:
       ordering = ['-fecha_hora']

   def __str__(self):
       return f"Voto de {self.cliente.nombre} - Copa: {self.copa.nombre} - Puntuación: {self.puntuacion}"
  
class CuentaBancaria(models.Model):
   BANCOS = [
       ('Caixa', 'Caixa'),
       ('BBVA', 'BBVA'),
       ('UNICAJA', 'UNICAJA'),
       ('ING', 'ING'),
   ]
   cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='cuenta_bancaria')
   numero_cuenta = models.CharField(max_length=20)
   banco = models.CharField(max_length=20, choices=BANCOS)

   def __str__(self):
       return f"{self.banco} - Cuenta de {self.cliente.nombre}"
