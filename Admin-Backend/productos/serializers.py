from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Categoria,Comentario,Escaneos,Favorito,Galeria,Local,Notificaciones,Permiso,Rol,Rolpermiso,Telefono,Usuario
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
class TCategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields='__all__'
class TComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comentario
        fields='__all__'
class TEscaneosSerializer(serializers.ModelSerializer):
     class Meta:
         model= Escaneos
         fields='__all__'
class TFavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Favorito
        fields='__all__'
class TGaleriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Galeria
        fields='__all__'
class TLocalSerializer(serializers.ModelSerializer):
    class Meta:
        model= Local
        fields='__all__'
class TNotificacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Notificaciones
        fields='__all__'
class TPermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Permiso
        fields='__all__'
class TRolSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rol
        fields='__all__'
class TRolpermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Rolpermiso
        fields='__all__'
class TTelefonoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Telefono
        fields='__all__'
class TUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields='__all__'
        
