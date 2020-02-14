from rest_framework import routers, serializers, viewsets

#---------------- AGREGANDO MODELOS ---------------------
from Profile.models import Profile
from Profile.models import ModelEstado
from Profile.models import ModelCiudad
from Profile.models import ModelEstadoCivil
from Profile.models import ModelGenero
from Profile.models import ModelOcupacion

class ProfileSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Profile
        fields = ('__all__')

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= ModelEstado
        fields= ('__all__')

class CiudadSerializer(serializers.ModelSerializer):
    class Meta:
        model= ModelCiudad
        fields= ('__all__')

class EstadoCSerializer(serializers.ModelSerializer):
    class Meta:
        model= ModelEstadoCivil
        fields= ('__all__')

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model= ModelGenero
        fields= ('__all__')

class OcupacionSerializer(serializers.ModelSerializer):
    class Meta:
        model= ModelOcupacion
        fields= ('__all__')

