from permisosturismo.models import Ciudadano, Domicilio,Evento,Permiso
from permisosturismo.serializers import CiudadanoSerializer, DomicilioSerializer, EventoSerializer, PermisoSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class CiudadanoViewSet(viewsets.ModelViewSet):
   "A continuación se encuentra la vista para crear, modificar, obtener o borrar los ciudadanos registrados en el sistema"
   queryset = Ciudadano.objects.all()
   serializer_class = CiudadanoSerializer
   filter_backends = [DjangoFilterBackend]
   filterset_fields = ['nroDoc']
 
class EventoViewSet(viewsets.ModelViewSet):
   "A continuación se encuentra la vista para crear, modificar, obtener o borrar los eventos registrados en el sistema"
   queryset = Evento.objects.all()
   serializer_class = EventoSerializer

class DomicilioViewSet(viewsets.ModelViewSet):
   "A continuación se encuentra la vista para crear, modificar, obtener o borrar los domicilios registrados en el sistema"
   queryset = Domicilio.objects.all()
   serializer_class = DomicilioSerializer
 
class PermisoViewSet(viewsets.ModelViewSet):
   "A continuación se encuentra la vista para crear, modificar, obtener o borrar los permisos registrados en el sistema"
   queryset = Permiso.objects.all()
   serializer_class = PermisoSerializer

   
