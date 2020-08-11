from django.urls import include, path
from . import views

urlpatterns = [
    path('lista_consultor/', views.lista_consultor, name='lista_consultor'),
    path('lista_servico/', views.lista_servico, name='lista_servico'),
]