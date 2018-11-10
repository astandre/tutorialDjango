from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import *
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .forms import *


# Create your views here.

def eventos_todos(request):
    """
    View of all events
    """
    eventos_list = Eventos.objects.all()
    template = loader.get_template('controlAsistencias/eventos_todos.html')
    context = {
        'eventos_list': eventos_list
    }
    return HttpResponse(template.render(context, request))


def evento(request, id_evento):
    """
    View of a event
    """
    evento_seleccionado = Eventos.objects.get(id_evento=id_evento)
    inscritos = Personas.objects.filter(evento__id_evento=id_evento)
    inscritos_totales = len(inscritos)

    template = loader.get_template('controlAsistencias/evento.html')
    context = {
        'evento': evento_seleccionado,
        'inscritos': inscritos,
        'inscritos_totales': inscritos_totales
    }
    return HttpResponse(template.render(context, request))


def inscritos_todos(request):
    """
    View of all events
    """
    inscritos_list = Personas.objects.all()
    template = loader.get_template('controlAsistencias/inscritos_todos.html')
    context = {
        'inscritos_list': inscritos_list
    }
    return HttpResponse(template.render(context, request))


def inscripcion_update(request, id_persona):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        instance = get_object_or_404(Personas, id_persona=id_persona)
        form = InscripcionUpdateForm(request.POST or None, instance=instance)
        # form = InscripcionForm(request.POST)
        # check whether it's valid:
        # print(id_persona)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # print(form.data)
            form.save()
            messages.success(request, 'Exito')
            return HttpResponseRedirect('/inscritos/')
        else:
            messages.warning(request, 'Error')
        # if a GET (or any other method) we'll create a blank form
        return render(request, 'controlAsistencias/inscripcion.html', {'form': form})
    else:
        form = InscripcionUpdateForm()
        persona = Personas.objects.only("cedula", "sexo", "nombre").get(id_persona=id_persona)
        # messages.success(request, 'Actualizacion completa')
        return render(request, 'controlAsistencias/inscripcion.html', {'form': form, "persona": persona})


def inscripcion_delete(request, id_persona):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        instance = get_object_or_404(Personas, id_persona=id_persona)
        print(instance)
        # form = InscripcionForm(request.POST)
        # check whether it's valid:
        if instance is not None:
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            instance.delete()
            messages.success(request, 'Exito')
            return HttpResponseRedirect('/inscritos/')
        else:
            messages.warning(request, 'Error')
        # if a GET (or any other method) we'll create a blank form
        return HttpResponseRedirect('/inscritos/')


def inscripcion(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InscripcionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            messages.success(request, 'Exito')
            return HttpResponseRedirect('/inscritos/')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = InscripcionForm()

    return render(request, 'controlAsistencias/inscripcion.html', {'form': form})


def buscar_evento(request):
    return render(request, 'controlAsistencias/buscar_evento.html')


@csrf_exempt
def evento_ajax(request):
    """
    Ajax View to get data
    """
    if request.is_ajax() == True:
        value = request.POST.getlist('evento')[0]
        try:
            evento = Eventos.objects.values("id_evento", "nombre").get(nombre__contains=value)
        except Eventos.DoesNotExist:
            resp = {"encontrado": False, "message": "Evento no encontrado"}
        else:
            resp = {"id": evento["id_evento"], "encontrado": True, "nombre": evento["nombre"]}
    return JsonResponse(resp, safe=False)
