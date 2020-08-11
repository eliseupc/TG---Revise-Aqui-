from django.urls import include, path
from . import views

urlpatterns = [
    path('lista_cliente/', views.lista_cliente, name='lista_cliente'),
]