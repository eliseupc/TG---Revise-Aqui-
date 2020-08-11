from django.urls import include, path
from . import views

urlpatterns = [
    path('cliente/', views.cliente, name='cliente'),
    path('consultor/', views.consultor, name='consultor'),
    path('servico/', views.servico, name='servico'),
    path('agenda/', views.agenda, name='agenda'),
    path('lista/', views.lista, name='lista'),
    path('editar/<int:id_agenda>/', views.editar, name='editar'),
    path('deletar/<int:id_agenda>/', views.deletar, name='deletar'),
    path('edita_cliente/<int:id_cliente>/', views.edita_cliente, name='edita_cliente'),
    path('deleta_cliente/<int:id_cliente>/', views.deleta_cliente, name='deleta_cliente'),
    path('edita_cliente_home/<int:id_cliente>/', views.edita_cliente_home, name='edita_cliente_home'),
    path('deleta_cliente_home/<int:id_cliente>/', views.deleta_cliente_home, name='deleta_cliente_home'),
    path('edita_consultor/<int:id_consultor>/', views.edita_consultor, name='edita_consultor'),
    path('deleta_consuktor<int:id_consultor>/', views.deleta_consultor, name='deleta_consultor'),
    path('edita_servico/<int:id_servico>/', views.edita_servico, name='edita_servico'),
    path('deleta_servico/<int:id_servico>/', views.deleta_servico, name='deleta_servico'),
    path('edita_usuario/<int:id_user>/', views.edita_usuario, name='edita_usuario'),
    path('deleta_usuario/<int:id_user>/', views.deleta_usuario, name='deleta_usuario'),
    
]