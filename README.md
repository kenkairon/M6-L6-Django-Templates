# M6-L6-Django-Templates
Educativo y de Aprendizaje Personal

---

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Configuración del Entorno](#configuración-del-entorno)
- [Activación del Entorno](#Activación-del-Entorno)
- [Configuración Inicial](#configuración-inicial)
- [Pasos del Proyecto](#pasos-del-proyecto)
  - [Configuración del Proyecto](#configuración-del-proyecto)
  - [Creación de Vistas y Modelos](#creación-de-vistas-y-modelos)
 

---

## Configuración del Entorno

1. Crear el entorno virtual:
   ```bash
   python -m venv venv

## Activación del Entorno

2. Activar el entorno virtual:
    ### Windows
    ```bash
    venv\Scripts\activate

## Configuración Inicial
## Instalar Django y Guardar dependencias

3. Intalación Django
    ```bash
    pip install django

4. Instalamos la actualizacion de pip
    ```bash
    python.exe -m pip install --upgrade pip

5. Si queremos saber las versiones de django y guardar lo que instalmos en requirements.txt
    ```bash
    python -m django --version
    pip freeze > requirements.txt

## Pasos del Proyecto

6. Hacemos la Instalación del proyecto_educativo
    ```bash
    django-admin startproject proyecto_educativo

7. Entramos a proyecto_educativo
    ```bash
    cd proyecto_eductativo

8. Hacemos la aplicación principal
    ```bash
    python manage.py startapp principal

9. Se corre la migración se crea la base de datos las tablas que vienen por defecto en django
    ```bash
    python manage.py migrate

10. Activamos el servidor solo para ver el localhost y el mensaje de Bienvenida
    ```bash
    python manage.py runserver

## Configuración del Proyecto

11. Creamos los templates en principal/templates/index.html
    ```bash
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Hola Mundo</h1>
    </body>
    </html>

12. en principal/views.py
    ```bash
    from django.shortcuts import render

    def home(request):
        return render(request, 'index.html')

13. En proyecto_educativo/urls.py
    ```bash
    from django.contrib import admin
    from django.urls import path, include
    from principal  import views
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', views.home,name='home'),
    ]

14.  En proyecto_educativo/setting.py vamos a registrar la aplicación
    ```bash
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'principal',
    ]
15. Activamos el servidor
    ```bash
    python manage.py runserver

16. En principal/models.py Configuramos el Modelo
    ```bash
    from .models import Estudiante

    def home(request):
        estudiantes = Estudiante.objects.all()
        return render(request, 'index.html', {'estudiantes': estudiantes})

17. Vamos al templates/index.html
    ```bash
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1>Hola Mundo</h1>
        {% for estudiante in estudiantes %}
        <li>{{estudiante.nombre}}</li>
        {{% endfor %}}
    </body>
    </html>

18. Hacemos la migración para que reconozca mis tablas estudiante
    ```bash
    python manage.py migrate

19. Ingresamos a la Shell para poblar información 
    ```bash
    python manage.py Shell

20. Ejecutamos en la Shell
    ```bash
    from principal.models import Estudiante
    estudiantes = [
        {'nombre': 'Juan', 'apellido': 'Pérez', 'correo': 'juan.perez@gmail.com', 'edad': 20},
        {'nombre': 'Ana', 'apellido': 'Gómez', 'correo': 'ana.gomez@gmail.com', 'edad': 22},
        {'nombre': 'Luis', 'apellido': 'Martínez', 'correo': 'luis.martinez@gmail.com', 'edad': 19},
        {'nombre': 'María', 'apellido': 'Rodríguez', 'correo': 'maria.rodriguez@gmail.com', 'edad': 21},
        {'nombre': 'Pedro', 'apellido': 'López', 'correo': 'pedro.lopez@gmail.com', 'edad': 23},
        {'nombre': 'Carla', 'apellido': 'Fernández', 'correo': 'carla.fernandez@gmail.com', 'edad': 24},
        {'nombre': 'Sofía', 'apellido': 'Hernández', 'correo': 'sofia.hernandez@gmail.com', 'edad': 20},
        {'nombre': 'Daniel', 'apellido': 'Ruiz', 'correo': 'daniel.ruiz@gmail.com', 'edad': 25},
        {'nombre': 'Lucía', 'apellido': 'Ramírez', 'correo': 'lucia.ramirez@gmail.com', 'edad': 18},
        {'nombre': 'Fernando', 'apellido': 'Castro', 'correo': 'fernando.castro@gmail.com', 'edad': 22},
        {'nombre': 'Paula', 'apellido': 'Ortiz', 'correo': 'paula.ortiz@gmail.com', 'edad': 21},
        {'nombre': 'Jorge', 'apellido': 'Silva', 'correo': 'jorge.silva@gmail.com', 'edad': 26},
        {'nombre': 'Valeria', 'apellido': 'Moreno', 'correo': 'valeria.moreno@gmail.com', 'edad': 19},
        {'nombre': 'Ignacio', 'apellido': 'Vega', 'correo': 'ignacio.vega@gmail.com', 'edad': 24},
        {'nombre': 'Camila', 'apellido': 'Díaz', 'correo': 'camila.diaz@gmail.com', 'edad': 23},
        {'nombre': 'Héctor', 'apellido': 'Cruz', 'correo': 'hector.cruz@gmail.com', 'edad': 27},
        {'nombre': 'Mónica', 'apellido': 'Navarro', 'correo': 'monica.navarro@gmail.com', 'edad': 22},
        {'nombre': 'Gabriel', 'apellido': 'Reyes', 'correo': 'gabriel.reyes@gmail.com', 'edad': 21},
        {'nombre': 'Elena', 'apellido': 'Torres', 'correo': 'elena.torres@gmail.com', 'edad': 20},
        {'nombre': 'Ramiro', 'apellido': 'García', 'correo': 'ramiro.garcia@gmail.com', 'edad': 25},
    ]

    for data in estudiantes:
        Estudiante.objects.create(**data)

    print("Datos ingresados con éxito.")
    exit()

21. Vamos en principal y creamos en templates/detalle.html
    ```bash
    {% extends 'base.html' %}

    {% block title %}Detalle de Estudiante{% endblock %}

    {% block content %}
    <h2>{{ estudiante.nombre }} {{ estudiante.apellido }}</h2>
    <p>Correo: {{ estudiante.correo }}</p>
    <p>Edad: {{ estudiante.edad }}</p>
    <p>Fecha de Registro: {{ estudiante.fecha_registro }}</p>
    <a href="{% url 'home' %}">Volver</a>
    {% endblock %}

22. Configuramos la vista principal/views.py
    ```bash
    from django.shortcuts import render, get_object_or_404
    from .models import Estudiante

    def home(request):
        estudiantes = Estudiante.objects.all()
        return render(request, 'index.html', {'estudiantes': estudiantes})

    def detalle_estudiante(request, estudiante_id):
        estudiante = get_object_or_404(Estudiante, pk=estudiante_id)
        return render(request, 'detalle.html', {'estudiante': estudiante})

23. Cambiamos la configuración proyecto_educativo/urls.py
     ```bash
    from django.contrib import admin
    from django.urls import path, include
    from principal  import views
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('principal.urls')),
    ]

24. Configuramos principal/urls.py
    ```bash
    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.home, name='home'),
        path('estudiante/<int:estudiante_id>/', views.detalle_estudiante, name='detalle_estudiante'),
    ]






