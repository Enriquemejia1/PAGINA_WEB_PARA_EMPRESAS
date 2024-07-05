from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.http import HttpRequest,HttpResponseRedirect
from .models import *
from .forms import *
from uuid import UUID
from django.contrib.auth import login, authenticate 

# Create your views here.


class Home(View):
    def get(self,request):
        try:
            form = BusquedaForm()
        #libros = Libro.objects.filter().order_by( "-calificacion")

            return render(request,"home.html",{"form":form})#"home.html,")

        except Exception as error:
            return render(request, 'error.html', {'error': error})

    def post(self, request:HttpRequest):
        try:
            form = BusquedaForm( request.POST)
           
            if form.is_valid():
                termino_busqueda = form.cleaned_data['terminodebusqueda']
                
                return HttpResponseRedirect(reverse('resultados',args=[termino_busqueda]))
            
            else:
                return render(request, 'agregar_libro.html', {'form': form })

            
        except Exception as error:
            return render(request, 'error.html', {'error': error})
        

class ResultadoBusqueda(View):
    def get(self,request, termino_busqueda : str):
        try:
            
            resultados = Empresa.objects.filter(perfil_empresa__categoria__nombre__contains = termino_busqueda)

            return render(request,"resultado.html", {'termino_busqueda': termino_busqueda, 'resultados': resultados})#"home.html,")

        except Exception as error:
            return render(request, 'error.html', {'error': error})
        

class Login(View):
    def get(self, request: HttpRequest):
        try:
            if request.user.is_authenticated:
                return HttpResponseRedirect(reverse('home'))

            form = LoginForm()

            return render(request, 'login.html', {'form': form})
        
        except Exception as error:
            return render(request,'error.html',{'error':error})
    
    def post(self, request: HttpRequest):
        try:
            form = LoginForm(request.POST)

            if form.is_valid():
               username = form.cleaned_data['username']
               password = form.cleaned_data['password']

               print(username)
               print(password)

              
               
               user = authenticate(request, username = username, password = password)

               if user is not None:
                   login(request, user)

                   return HttpResponseRedirect(reverse('home'))
               else:
                   return render(request, 'login.html', {'form':form, 'aunthentication_error': True})
                   

            else:
                return render(request, 'login.html', {'form':form})
       
        except Exception as error:
            return render(request,'error.html',{'error':error})