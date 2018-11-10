from django.urls import path
from controlAsistencias import views

urlpatterns = [
    path(r'todos/', views.eventos_todos, name='eventos_todos'),
    path(r'inscritos/', views.inscritos_todos, name='inscritos_todos'),
    path(r'inscripcion/update/<int:id_persona>', views.inscripcion_update, name='inscripcion_update'),
    path(r'inscripcion/delete/<int:id_persona>', views.inscripcion_delete, name='inscripcion_delete'),
    path(r'evento/<int:id_evento>', views.evento, name='evento'),
    path(r'inscripcion/', views.inscripcion, name='inscripcion'),
    path(r'buscar/', views.buscar_evento, name='buscar_evento'),
    path(r'ajax/buscar/', views.evento_ajax, name='evento_ajax')

]
