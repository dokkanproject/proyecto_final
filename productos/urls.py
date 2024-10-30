from django.urls import path
from productos import views

app_name = 'productos'

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('productos/about/', views.sobreMi, name='sobreMi'),
    path('productos/add_product/', views.agregarProductos, name='agregar_producto'),
    path('productos/buscar_producto/', views.buscarProductos, name='buscar_producto'),
    path('productos/ver_producto/<int:id>', views.verProducto, name='ver_producto'),
    path('productos/eliminar_producto/<int:id>', views.eliminarProducto, name='eliminar_producto'),
    path('productos/editar_producto/<int:id>', views.editarProducto, name='editar_producto'),
]
