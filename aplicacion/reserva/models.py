from django.db import models

class Campista(models.Model):
    nombre_completo = models.CharField(max_length=200)  # Nombre completo del campista
    correo_electronico = models.EmailField(unique=True)  # Correo electrónico (único)
    telefono = models.CharField(max_length=20)  # Teléfono del campista
    direccion = models.TextField(blank=True, null=True)  # Dirección (opcional)

    def __str__(self):
        return self.nombre_completo  # Devuelve el nombre del campista cuando se imprima

class Reserva(models.Model):
    # Opciones para el tipo de alojamiento
    ALOJAMIENTO_CHOICES = [
        ('Tienda', 'Tienda'),
        ('Cabaña', 'Cabaña'),
        ('Caravana', 'Caravana'),
    ]

    # Opciones para el estado de la reserva
    ESTADO_CHOICES = [
        ('Confirmada', 'Confirmada'),
        ('Pendiente', 'Pendiente'),
        ('Cancelada', 'Cancelada'),
    ]
    
    # Relación con el campista: una reserva pertenece a un campista
    campista = models.ForeignKey(Campista, on_delete=models.CASCADE, related_name='reservas')
    fecha_inicio = models.DateField()  # Fecha de inicio de la reserva
    fecha_fin = models.DateField()  # Fecha de fin de la reserva
    tipo_alojamiento = models.CharField(max_length=10, choices=ALOJAMIENTO_CHOICES)  # Tipo de alojamiento
    numero_personas = models.IntegerField()  # Número de personas en la reserva
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES)  # Estado de la reserva
    observaciones = models.TextField(blank=True, null=True)  # Observaciones adicionales (opcional)
    
    def __str__(self):
        return f"Reserva de {self.campista.nombre_completo} del {self.fecha_inicio} al {self.fecha_fin}"
