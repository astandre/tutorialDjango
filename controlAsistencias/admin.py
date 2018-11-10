from django.contrib import admin
from .models import *


# Register your models here.

class ActividadesInline(admin.TabularInline):
    model = Actividades
    extra = 5


class EventsAdmin(admin.ModelAdmin):
    inlines = [ActividadesInline]
    list_display = ('nombre', 'descripcion', 'hora_inicio')
    list_filter = ['nombre']
    search_fields = ['nombre']


class PersonsAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'sexo')
    list_filter = ['sexo', 'evento__nombre']
    search_fields = ['cedula', 'nombre']


class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'hora_inicio', 'evento')
    list_filter = ['evento__nombre']
    search_fields = ['titulo']






admin.site.register(Eventos, EventsAdmin)
admin.site.register(Personas, PersonsAdmin)
admin.site.register(Actividades, ActivitiesAdmin)
