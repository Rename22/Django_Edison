# URLS especificas de la aplicacion
from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio),  # Página de inicio
    # Campesino
    path('nuevocampesino/', views.nuevocampesino),  # Formulario para agregar nuevo campista
    path('listadocampesino/', views.listadocampesino),  # Listado de campistas
    path('guardarcampesino/', views.guardarcampesino),  # Guardar nuevo campista
    path('editarcampesino/<campista_id>', views.editarcampesino),  # Editar campista
    path('procesarEdicioncampesino/', views.procesarEdicioncampesino),  # Procesar edición de campista
    path('eliminarcampesino/<campista_id>', views.eliminarcampesino),  # Eliminar campista

    # Reserva
    path('nuevoreserva/', views.nuevoreserva),  # Formulario para agregar nueva reserva
    path('listadoreserva/', views.listadoreserva),  # Listado de reservas
    path('guardarreserva/', views.guardarreserva),  # Guardar nueva reserva
    path('editarreserva/<reserva_id>', views.editarreserva),  # Editar reserva
    path('procesarEdicionreserva/', views.procesarEdicionreserva),  # Procesar edición de reserva
    path('eliminarreserva/<reserva_id>', views.eliminarreserva),  # Eliminar reserva
]
