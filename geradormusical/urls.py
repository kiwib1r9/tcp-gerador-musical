from django.urls import path
from . import views

urlpatterns = [
    path('', views.TelaDeEntrada.as_view(), name='TelaDeEntrada'),
    path('rep', views.TelaDeReproducao.as_view(), name='TelaDeReproducao'),
]