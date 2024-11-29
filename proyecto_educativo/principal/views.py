from django.shortcuts import render, get_object_or_404
from .models import Estudiante

def home(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'index.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, estudiante_id):
    estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
    return render(request, 'detalle.html', {'estudiante': estudiante})
    