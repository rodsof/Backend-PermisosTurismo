from permisosturismo.models import Ciudadano, Domicilio, Evento, Permiso
from rest_framework_json_api import serializers



class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = "__all__"


class PermisoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permiso
        fields = "__all__"


class CiudadanoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ciudadano
        fields = "__all__"

class DomicilioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Domicilio
        fields = "__all__"
