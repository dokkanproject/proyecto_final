from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('perfil/editar/', views.editarPerfil, name='editar_perfil'),
    path('perfil/editar/cambiar_password/', views.CambiarPassword.as_view(), name='cambiar_password'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('buscar_usuarios/', views.buscarUsuarios, name='buscar_usuarios'),
    path('ver_perfil/<int:id>', views.verPerfil, name='ver_perfil'),
]
