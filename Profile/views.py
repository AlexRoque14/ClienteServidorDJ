from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status
from rest_framework import generics

from Profile.models import Profile
from Profile.models import ModelEstado
from Profile.models import ModelCiudad
from Profile.models import ModelEstadoCivil
from Profile.models import ModelGenero
from Profile.models import ModelOcupacion

from Profile.serializer import ProfileSerializers
from Profile.serializer import EstadoSerializer
from Profile.serializer import EstadoCSerializer
from Profile.serializer import CiudadSerializer
from Profile.serializer import GeneroSerializer
from Profile.serializer import OcupacionSerializer

class ProfileList(APIView):
    #METODO GET PARA SOLICITAR INFO
    def get (self , request , format = None):
        print("Metodo get filter")
        queryset = Profile.objects.filter(delete = False)
        #many true si se aplica retornos multiples objetos
        serializer = ProfileSerializers(queryset, many= True)
        return Response(serializer.data)

    #METODO POST PARA ENVIAR INFORMACION
    def post (self, request , format = None):
        serializer = ProfileSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
    #Metodo GET
    def get(self, request, format = None):
        print("Metodo get filter")
        queryset = ModelEstado.objects.filter(delete = False)

        serializer = EstadoSerializer(queryset, many = True)
        return Response(serializer.data)
    
       #METODO POST PARA ENVIAR INFORMACION
    def post (self, request , format = None):
        serializer = EstadoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CiudadList(APIView):
    #Metodo GET
    def get(self, request, format = None):
        print("Metodo get filter")
        queryset = ModelCiudad.objects.filter(delete = False)

        serializer = CiudadSerializer(queryset, many = True)
        return Response(serializer.data)
    
       #METODO POST PARA ENVIAR INFORMACION
    def post (self, request , format = None):
        serializer = CiudadSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoCList(APIView):
    #Metodo GET
    def get(self, request, format = None):
        print("Metodo get filter")
        queryset = ModelEstadoCivil.objects.filter(delete = False)

        serializer = EstadoCSerializer(queryset, many = True)
        return Response(serializer.data)
    
       #METODO POST PARA ENVIAR INFORMACION
    def post (self, request , format = None):
        serializer = EstadoCSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GeneroList(APIView):
    #Metodo GET
    def get(self, request, format = None):
        print("Metodo get filter")
        queryset = ModelGenero.objects.filter(delete = False)

        serializer = GeneroSerializer(queryset, many = True)
        return Response(serializer.data)
    
       #METODO POST PARA ENVIAR INFORMACION
    def post (self, request , format = None):
        serializer = GeneroSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):
    #Metodo GET
    def get(self, request, format = None):
        print("Metodo get filter")
        queryset = ModelOcupacion.objects.filter(delete = False)

        serializer = OcupacionSerializer(queryset, many = True)
        return Response(serializer.data)
    
       #METODO POST PARA ENVIAR INFORMACION
    def post (self, request , format = None):
        serializer = OcupacionSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


