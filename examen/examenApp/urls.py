from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('copas/', views.lista_copas, name='lista_copas'),
    path('favoritas/', views.lista_favoritas, name='lista_favoritas'),
    path('copas-votados/<int:cliente_id>/', views.copas_votadas_con_puntuacion, name='copas_votadas_con_puntuacion'),
    path('cliente-sin-votaciones/', views.clientes_sin_votaciones, name='clientes_sin_votaciones'),
    path('cuentas-bancarias/<str:texto>/', views.cuentas_bancarias_por_banco_y_nombre, name='por_banco_y_nombre'),
    path('copas-con-media-votacion/', views.copas_con_media_votacion, name='con_media_votacion'),
    path('ultimo-voto-copa/<int:copa_id>/', views.ultimo_voto_copas, name='ultimo_voto_copas'),
]

handler404 = 'examenApp.views.handler_404'
handler500 = 'examenApp.views.handler_500'
handler403 = 'examenApp.views.handler_403'
handler400 = 'examenApp.views.handler_400'