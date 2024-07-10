from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('login', Login.as_view(), name='login'),
    path('singup', Singup.as_view(), name='singup'),
    path('crearperfil', Crearperfil.as_view(), name='crearperfil'),
#    path('', ResultadoBusqueda.as_view(), name = 'resultados'),
    path('buscar/<str:termino_busqueda>/resultado',ResultadoBusqueda.as_view(), name= 'resultados' ),

]