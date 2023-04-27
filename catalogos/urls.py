from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello ),
    path('laptops', views.laptopsListar ),
    
]
