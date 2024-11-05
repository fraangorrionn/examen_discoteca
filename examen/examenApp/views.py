from django.db.models import Q, Count, Sum, F , Prefetch
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Cliente, Copa, Favoritas, CuentaBancaria, Voto

# Vista principal que redirige al índice de URLs.
def index(request):
    return render(request, 'index.html')

def lista_clientes(request):
    clientes = Cliente.objects.prefetch_related('copas_favoritas').all()
    return render(request, 'lista_clientes.html', {'clientes': clientes})

def lista_copas(request):
    copas = Copa.objects.order_by('-precio')
    return render(request, 'lista_copas.html', {'copas': copas})

def lista_favoritas(request):
    favoritas = Favoritas.objects.select_related('cliente', 'copa').filter(prioridad__gte=2)
    return render(request, 'lista_favoritas.html', {'favoritas': favoritas})

#El último voto que se realizó en un modelo principal en concreto, y mostrar el comentario, la votación e información
# del usuario o cliente que lo realizó: 1.5 puntos
def ultimo_voto_copas(request, copa_id):
    copa = get_object_or_404(Copa, id=copa_id)
    ultimo_voto = copa.votos.select_related('cliente').first()
    return render(request, 'ultimo_voto_copas.html', {'copa': copa, 'ultimo_voto': ultimo_voto})


#Todos los modelos principales que tengan votos con una puntuación numérica menor a 3 y que realizó un usuario o 
# cliente en concreto: 1.5 puntos
def copas_votadas_con_puntuacion(request, cliente_id):
    copas = Copa.objects.filter(votos__cliente_id=cliente_id, votos__puntuacion=3).distinct()
    return render(request, 'copas_votadas_con_puntuacion.html', {'copas': copas})

#Todos los usuarios o clientes que no han votado nunca y mostrar información sobre estos usuarios y clientes al completo: 1.5 puntos
def clientes_sin_votaciones(request):
    clientes = Cliente.objects.filter(voto__isnull=True).select_related('cuenta_bancaria')
    return render(request, 'clientes_sin_votaciones.html', {'clientes': clientes})

#Obtener las cuentas bancarias que sean de la Caixa o de Unicaja y que el propietario tenga un nombre que contenga
# un texto en concreto, por ejemplo “Juan”: 1.5 puntos
def cuentas_bancarias_por_banco_y_nombre(request, texto):
   cuentas = CuentaBancaria.objects.filter(banco__in=['Caixa', 'UNICAJA'], cliente__nombre__icontains=texto)
   return render(request, 'por_banco_y_nombre.html', {'cuentas': cuentas})

#Obtener los votos de los usuarios que hayan votado a partir del 2023 con una puntuación numérica igual a 5  y que tengan 
# asociada una cuenta bancaria. 1.5 puntos
#def Votos_a_partir_2023(request):
#    votos = Cliente.objects.prefetch_related(Prefetch('cliente_voto' , 'banco_cliente'))
#    votos = votos.filter()
#    return render(request, 'Votos_a_partir_2023.html', {'votos': votos})

#Obtener todos los modelos principales que tengan una media de votaciones mayor del 2,5: 1.5 punto
from django.db.models import Avg
def copas_con_media_votacion(request):
   copas = Copa.objects.annotate(media_votacion=Avg('votos__puntuacion')).filter(media_votacion__gt=2.5)
   return render(request, 'con_media_votacion.html', {'copas': copas})

# Errores
def handler_404(request, exception):
    """Muestra una página personalizada para el error 404 (página no encontrada)."""
    return render(request, '404.html', status=404)

def handler_500(request):
    """Muestra una página personalizada para el error 500 (error interno del servidor)."""
    return render(request, '500.html', status=500)

def handler_403(request, exception):
    """Muestra una página personalizada para el error 403 (prohibido)."""
    return render(request, '403.html', status=403)

def handler_400(request, exception):
    """Muestra una página personalizada para el error 400 (solicitud incorrecta)."""
    return render(request, '400.html', status=400)
