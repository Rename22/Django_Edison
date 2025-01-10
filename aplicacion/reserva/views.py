from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Campista, Reserva

# Vista de inicio
def inicio(request):
    return render(request, 'inicio.html')

# Campistas -------------------------------------------------------------------------------------------------

# Vista para mostrar el formulario de nuevo Campista
def nuevocampesino(request):
    return render(request, 'nuevocampesino.html')

# Vista para mostrar la lista de Campistas
def listadocampesino(request):
    campistasBdd = Campista.objects.all()
    return render(request, 'listadocampesino.html', {'campistas': campistasBdd})

# Vista para guardar un nuevo Campista
def guardarcampesino(request):
    nombre_completo = request.POST['nombre_completo']
    correo_electronico = request.POST['correo_electronico']
    telefono = request.POST['telefono']
    direccion = request.POST.get('direccion', '')

    Campista.objects.create(
        nombre_completo=nombre_completo,
        correo_electronico=correo_electronico,
        telefono=telefono,
        direccion=direccion
    )
    messages.success(request, "Campista Guardado Exitosamente")
    return redirect('/listadocampesino')

# Vista para eliminar un Campista
def eliminarcampesino(request, campista_id):
    campistaEliminar = Campista.objects.get(id=campista_id)
    campistaEliminar.delete()
    messages.success(request, "Campista Eliminado Exitosamente")
    return redirect('/listadocampesino')

# Vista para editar un Campista
def editarcampesino(request, campista_id):
    campistaEditar = Campista.objects.get(id=campista_id)
    return render(request, 'editarcampesino.html', {'campista': campistaEditar})

# Vista para procesar la edición de un Campista
def procesarEdicioncampesino(request):
    campista = Campista.objects.get(id=request.POST['id'])
    campista.nombre_completo = request.POST['nombre_completo']
    campista.correo_electronico = request.POST['correo_electronico']
    campista.telefono = request.POST['telefono']
    campista.direccion = request.POST.get('direccion', '')

    campista.save()
    messages.success(request, "Campista Actualizado Exitosamente")
    return redirect('/listadocampesino')

# Reservas ---------------------------------------------------------------------------------------------------

# Vista para mostrar el formulario de nueva Reserva
def nuevoreserva(request):
    campistas = Campista.objects.all()  # Obtener todos los campistas
    return render(request, 'nuevoreserva.html', {'campistas': campistas})

# Vista para mostrar la lista de Reservas
def listadoreserva(request):
    reservasBdd = Reserva.objects.all()
    return render(request, 'listadoreserva.html', {'reservas': reservasBdd})

# Vista para guardar una nueva Reserva
def guardarreserva(request):
    campista_id = request.POST['campista']
    fecha_inicio = request.POST['fecha_inicio']
    fecha_fin = request.POST['fecha_fin']
    tipo_alojamiento = request.POST['tipo_alojamiento']
    numero_personas = request.POST['numero_personas']
    estado = request.POST['estado']
    observaciones = request.POST.get('observaciones', '')

    campista = Campista.objects.get(id=campista_id)

    Reserva.objects.create(
        campista=campista,
        fecha_inicio=fecha_inicio,
        fecha_fin=fecha_fin,
        tipo_alojamiento=tipo_alojamiento,
        numero_personas=numero_personas,
        estado=estado,
        observaciones=observaciones
    )
    messages.success(request, "Reserva Guardada Exitosamente")
    return redirect('/listadoreserva')

# Vista para eliminar una Reserva
def eliminarreserva(request, reserva_id):
    reservaEliminar = Reserva.objects.get(id=reserva_id)
    reservaEliminar.delete()
    messages.success(request, "Reserva Eliminada Exitosamente")
    return redirect('/listadoreserva')

# Vista para editar una Reserva
def editarreserva(request, reserva_id):
    reservaEditar = Reserva.objects.get(id=reserva_id)
    campistas = Campista.objects.all()  # Obtener todos los campistas
    return render(request, 'editarreserva.html', {'reserva': reservaEditar, 'campistas': campistas})

# Vista para procesar la edición de una Reserva
def procesarEdicionreserva(request):
    reserva = Reserva.objects.get(id=request.POST['id'])
    reserva.fecha_inicio = request.POST['fecha_inicio']
    reserva.fecha_fin = request.POST['fecha_fin']
    reserva.tipo_alojamiento = request.POST['tipo_alojamiento']
    reserva.numero_personas = request.POST['numero_personas']
    reserva.estado = request.POST['estado']
    reserva.observaciones = request.POST.get('observaciones', '')

    reserva.save()
    messages.success(request, "Reserva Actualizada Exitosamente")
    return redirect('/listadoreserva')
