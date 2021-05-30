# Backend-PermisosTurismo

Hola! Este repositorio contiene todo el código correspondiente a la API Hateoas creada con Django para resolver la consigna del Tema 2 del Primer Parcial de Sistemas Distribuidos II.

## Comenzando 🚀

Estas instrucciones permiten obtener una copia del proyecto en funcionamiento en su máquina.
Algunos requisitos son propios del funcionamiento de la API y otros fueron necesarios para realizar el deployment en Heroku.


Entrar a **https://permisosturismo.herokuapp.com/** para visitar el deploy del proyecto.


### Pre-requisitos 📋

¿Qué cosas se necesitan para ejecutar la API y cómo instalarlas?

```
pip install asgiref
pip install dj-database-url
pip install django
pip install django-cors-headers
pip install django-filter
pip install djangorestframework
pip install djangorestframework-jsonapi
pip install gunicorn
pip install inflection
pip install psycopg2
pip install psycopg2-binary
pip install pytz
pip install sqlparse
pip install typing-extensions
pip install whitenoise
```

### Instalación 🔧

Clonar el repositorio desde Github

```
git clone https://github.com/rodsof/Backend-PermisosTurismo.git
```

Configurar la base de datos PostgreSQL ejecutando las migraciones

```
python3 manage.py makemigrations
python3 manage.py migrate
```

El framework utilizado nos provee un modo administrador, si se quiere configurarlo se debe ingresar un usuario, un mail y una contraseña

```
python3 manage.py createsuperuser
```

## Ejecutar el servidor ⚙️

Se podrá acceder al servidor en localhost:8000

```
python3 manage.py runserver
```

## Construido con 🛠️


* [Django](https://www.djangoproject.com/) - Framework web usado
* [Pip](https://pip.pypa.io/en/stable/) - Manejador de dependencias
* [Heroku](https://www.heroku.com/python) - Usado para el deployment
* [PostgreSQL](https://www.postgresql.org/docs/) - Gestión de base de datos
* [Django-Filter](https://django-filter.readthedocs.io/en/stable/) - Permite filtrar según campos del modelo de datos
* [SQLParse](https://github.com/andialbrecht/sqlparse) - Parser SQL


## Necesario para el deploy en Heroku:
* [Gunicorn](https://gunicorn.org/) - Servidor web de producción recomendado por Heroku para apps hechas con Django
* [Dj Database URL(https://github.com/kennethreitz/dj-database-url) - Utilidad para gestionar la conexión a la base de datos
* [Whitenoise](http://whitenoise.evans.io/en/stable/) - Utilidad para servir archivos estáticos en producción
* [Psycopg2](https://www.psycopg.org/) - Driver PostgreSQL para Python
* [Django Cors Headers](https://github.com/adamchainz/django-cors-headers) - Agrega los headers de tipo Cross-Origin Resource Sharing (CORS) a las respuestas

## Incluido con la instalación de Django
* [Asgiref](https://github.com/django/asgiref) - Sirve para implementar vistas asincrónicas en Django
* [Inflection](https://inflection.readthedocs.io/en/latest/) - Librería para formateo de strings
* [Pytz](https://pythonhosted.org/pytz/) - Librería para zonas horarias
* [Typing Extensions](https://github.com/python/typing/blob/master/typing_extensions/README.rst) - Módulo de sugerencias para el tipeo de código

## Alumna 👧

* **Sofía Rodríguez** - [rodsof](https://github.com/rodsof)


## Links relacionados 🔖
* Código Frontend: https://github.com/rodsof/Frontend-PermisosTurismo.git
* Acceso al sistema: https://frontend-permisos-turismo.vercel.app/



