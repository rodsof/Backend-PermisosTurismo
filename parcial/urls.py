from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from permisosturismo import views

router = routers.DefaultRouter()
router.register(r'permisos', views.PermisoViewSet)
router.register(r'eventos', views.EventoViewSet)
router.register(r'ciudadanos', views.CiudadanoViewSet)
router.register(r'domicilios', views.DomicilioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
