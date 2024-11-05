from django.contrib import admin
from .models import ( 
    Cliente,
    Copa,
    Favoritas,
    Voto, 
    CuentaBancaria, 
)
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Copa)
admin.site.register(Favoritas)
admin.site.register(Voto)
admin.site.register(CuentaBancaria)
