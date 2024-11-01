from django.contrib import admin
from django.urls import path, include
from productos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),
    path('about/', views.sobreMi, name='sobreMi'),
    path('add_product/', views.agregarProductos, name='agregar_producto'),
    path('buscar_producto/', views.buscarProductos, name='buscar_producto'),
    path('ver_producto/<int:id>', views.verProducto, name='ver_producto'),
    path('eliminar_producto/<int:id>', views.eliminarProducto, name='eliminar_producto'),
    path('editar_producto/<int:id>', views.editarProducto, name='editar_producto'),
    path('usuarios/',include('usuarios.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)