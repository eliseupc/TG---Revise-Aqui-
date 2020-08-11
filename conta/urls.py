from django.urls import include, path
from . import views

urlpatterns = [
    path('novo-usuario/', views.add_usuario, name='add_usuario'),
    path('login-usuario/', views.user_login, name='user_login'),
    path('logout-usuario/', views.logout_user, name='logout_user'),
    path('lista_usuario/', views.lista_usuario, name='lista_usuario'),
]