from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('estudiante/<int:estudiante_id>/', views.detalle_estudiante, name='detalle_estudiante'),
]