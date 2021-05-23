from permisosturismo.models import Ciudadano, Domicilio,Evento,Permiso
from permisosturismo.serializers import CiudadanoSerializer, DomicilioSerializer, EventoSerializer, PermisoSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class CiudadanoViewSet(viewsets.ModelViewSet):
   queryset = Ciudadano.objects.all()
   serializer_class = CiudadanoSerializer
   filter_backends = [DjangoFilterBackend]
   filterset_fields = ['nroDoc']
 
class EventoViewSet(viewsets.ModelViewSet):
   queryset = Evento.objects.all()
   serializer_class = EventoSerializer

class DomicilioViewSet(viewsets.ModelViewSet):
   queryset = Domicilio.objects.all()
   serializer_class = DomicilioSerializer
 
class PermisoViewSet(viewsets.ModelViewSet):
   queryset = Permiso.objects.all()
   serializer_class = PermisoSerializer

   
