from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('login', Login.as_view(), name='login'),
#    path('', ResultadoBusqueda.as_view(), name = 'resultados'),
    path('buscar/<str:termino_busqueda>/resultado',ResultadoBusqueda.as_view(), name= 'resultados' ),

]