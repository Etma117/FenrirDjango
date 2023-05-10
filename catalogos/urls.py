from django.urls import path


from .import views

urlpatterns = [
    path('', views.home, name='home' ),
    path('productos/', views.productosListar, name='productos' ),
    path('productosCrear', views.productosCrear, name= 'productosCrear'),
    path('productosModificar/<int:id>/', views.productosModificar, name="productosEditar"),
    path('productosEliminar/<int:pk>/', views.productosEliminar, name='productosEliminar'),

] 
