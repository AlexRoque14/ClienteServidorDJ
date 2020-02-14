from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets
#from Profile.views import CustonAuthToken

from Profile import views 

urlpatterns = [
    #re_path(r'Login/$', CustonAuthToken.as_view()),
    #Hola soy Alexis

    re_path(r'example_profile/$', views.ProfileList.as_view()),
    re_path(r'example_ciudad/$', views.CiudadList.as_view()),
    re_path(r'example_estado/$', views.EstadoList.as_view()),
    re_path(r'example_estadoC/$', views.EstadoCList.as_view()),
    re_path(r'example_genero/$', views.GeneroList.as_view()),
    re_path(r'example_ocupacion/$', views.OcupacionList.as_view())
]