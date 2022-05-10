# Instalando Django

``` cmd
pip install django
```

Para crear un proyecto en Django

``` cmd
django-admin startproject {Nombre_del_Proyecto}
```

Correr el servidor de Django

``` cmd
cd {Nombre_del_Proyecto}
py manage.py runserver
```

Si lo desea se puede cambiar el nombre de la carpeta app/app por config u otro de su preferencia. Al cambiarlo asegurarse de que todas las referencias a app ahora son config

# Settings.py

En este archivo Django guarda toda la configuracion de nuestra aplicacion.

- Por defecto crea una base de datos SQLite, esta puede ser cambiada por otro tipo o agregar diferentes bases de datos.
- En este arhivo se da carga el primer archivo de rutas el cual contendra todas rutas dentro del proyecto.
- En este archivo se agregan las aplicaciones instaladas en nuestro proyecto, esta es la forma en que django permite escalar los proyectos organizando asi los diferentes modulos en la aplicacion.
- Tambien contendra todos los middlewares activos en el sistema
- Conteniene la configuracion de internacionalizacion.
- Contiene la configuracion para la validacion de las contraseñas

En fin, es uno de los archivos mas importantes. Muchas librerias necesitan de la configuracion de variables en la misma, como por ejemplo el **SWAGGER OPEN API**


# Configurar Base de Datos

Para configurar una base de datos en el proyecto es se puede configurar el archivo *setting.py* o se puede crear un archivo aparte y hacerle referencia en el *setting.py*

Al finalizar de configurar la base de datos se debe correr las migraciones

``` cmd
py manage.py migrate
```

# Aplicaciones

Una aplicacion es un contenedor que tendra varios archivos (rutas, modelos, controladores, etc) . Para crear una aplicacion se corre el comando

``` cmd
py manage.py startapp {nombre_aplicacion}
```

Para integrar la nueva aplicacion al proyecto se debe ir al *setting.py* y en la variable de aplicaciones instaladas incorporar la misma.

**Notas:**

- Importante que el nombre de la aplicacion creada coincida con el nombre de la aplicacion colocada en la lista de aplicaciones, para esto revisar el *app.py*



# Modelos
Para crear los modelos se crea una nueva aplicacion y en el archivo models.py se crean los modelos de la siguiente manera

``` python
#Clase que plantea los atributos del modelo
class Estudiante(models.Model):
    nombre = models.CharField()
    edad = models.IntegerField()
    
    #Clase para configurar la entidad
    class Meta:
        verbose_name = 'Estudiante'
```

Una vez declarados los modelos se corre

``` cmd
py manage.py makemigrations
```

Para actualizar las migraciones y que correspondan con el diseño de modelos. Posteriormente si lo desea se hacen las migraciones en la base de datos.

Los modelos se pueden relacionar unos con otros

``` python
class HasTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #Para heredar de la clase de forma abstracta
        ordering = ['updated_at']

class Tag(HasTimeStamp):
    name = models.CharField(max_length=255,unique=True)

class NoteBook(HasTimeStamp):
    titulo = models.CharField(max_length=250,default='Nuevo Libro de Notas')

class Note(HasTimeStamp):
    titulo = models.CharField(max_length=255,default='Nueva Nota')
    texto = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)
    notebook = models.ForeignKey(NoteBook,on_delete=models.SET_NULL,null=True)

```

En caso de relaciones de muchos a muchos se crea por defecto una tabla intermedia. Si se desea agregar atributos a esta tabla intermedia se recomienda crear un modelo y relacionarlo por medio de llaves foraneas.

# Django ORM

El ORM de django mapea la base de datos y permite realizar consultas, inserciones, eliminaciones y actualizaciones mediante un modelo de la misma

``` python
#Listar
Tag.objects.all()
Tag.objects.get(pk=1) #Obtener Elemente por PK
Tag.objects.filter() #Filtrar Datos
Tag.objects.filter().count() #Contar Datos

#Insertar
t = Tag(titulo='Redes')
t = Tag()
t.titulo='Redes'
t.save() #Guardar en Base de Datos

#Actualizar
t.titulo='Redes de Computadoras'
t.save() #Actualizar en Base de Datos

#Eliminar
t.delete() #Eliminar el Registro de la Base de Datos

```

# Django Test
Para correr pruebas en django es necesario ir al archivo *test.py* que se encuentra en cada aplicacion e incorporar todo el archivo *wsgi.py* que se encuentra en el *config*

``` python

```

# Panel de Administracion

El panel de administracion viene por defecto en Django, permite actualizar la base de datos de forma facil en caso de una emergencia y desarrollo del proyecto.

Para incorporar modelos al panel de administracion debemos ir al *admin.py* y seguir lo siguientes pasos

``` python
from models import *

#Register Models Here
admin.site.register(Tag)
admin.site.register(NoteBook)
admin.site.register(Note)

```

Para poder entrar al panel de administracion es necesario crear un usuario y una contraseña, para esto se debemos crear un superusuario

``` cmd
py manage.py createsuperuser
```

La consola pedira diferentes datos como nombre de usuario, correo y contraseña. Para acceder al administrador ir a */admin*

# URL
Cuando una pagina es solicitada se crea un **HttRequest** el cual contiene todos los datos de la petición, el mismo tiene que ser el primer argumento de las funciones de la vista. Siempre la funcion debera retornar un **HttpResponse**.

Las urls se pueden modularizar,para esto se puede crear un archivo urls.py en cada aplicacion e incluir en el mismo las diferentes urls

``` python
# notebook/url.py
from django.urls import path
from core.notebook.views import vista_basada_en_funcion

# mismo nombre de variable que en config/urls.py
urlpatterns = [
    path('prueba/',vista_basada_en_funcion)
]

# config/urls.py
# Importar libreria include

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/',include('core.notebook.urls'))
]

#agragar nombre a la URL
path('notebooks',url_notebooks,name='all_notebooks')

#se utiliza para agregar un namespace a las rutas
app_name='notebook' #notebook:all_notebooks

#otra forma es utilizar el include
 path('',include('core.notebook.urls',namespace='notebook'))

```

# Vistas

Las vistas son las encargadas de capturar la solicitud y responderla (controladores). Las misma puden ser de dos tipos.

``` python
#views.py
#Vistas basadas en funcion
def vista_basada_en_funcion(request):
    return HttpResponse('Hola esta es mi primera URL')

#Vistas basadas en clases

```
Una vez hecha la vista esta debe ser incluida en el archivo de rutas.

``` python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('prueba/',vista_basada_en_funcion)
]

```

La vista puede retornar diferentes tipos de objetos, por ejemplo **HttpResponse, JsonResponse**.

 # Plantillas

 Para trabajar con plantillas crearemos una carpeta la cual contendra todos las plantillas de la aplicacion. Para incluir los direcctorios vamos al settings.py y en la variable TEMPLATES en el valor DIRS agregamos los directorios.

 ``` python
 TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [Path.joinpath(BASE_DIR,'/core/notebook/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
 ```

Para devolver una plantilla se debe usar la funcion render como se muestra

``` python
def all_notes_template(request):
    notes= Note.objects.all()
    #Se para el request, la direccion del html y la data (opcional)
    return render(request,'list.html',notes)

```

Para que el codigo anterior funcione se necesita crear un archivo .html en las carpetas como plantillas. En las plantillas se tutiliza **{% if for else ... %}** y **{{ para variables }}**

A las plantillas se les puede aplicar herencia, mediante el uso de **{% block %}** y **{% extends %}**

``` python
#notes_layout.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pagina Principal de Notas</title>
</head>
<body>
{% block container_notes %}
    <p>Container Vacio</p>
{% endblock %}
</body>
</html>


#all_notes.html
{% extends 'notes_layout.html' %}

{% block container_notes %}
    <h3>Lista de Notas</h3>
    {% if notes %}
        {% for note in notes %}
            <li>{{ note }}</li>
        {% endfor %}
    {% else %}
        <p>No existen notas</p>
    {% endif %}

{% endblock %}
```

# Archivos Estaticos 

Primero verificar que **django.contrib.staticfiles** se encuente en el **INSTALLED_APPS** , comprobar que **STATIC_URL** se encuentre inicializado, por ultimo utilizar *static* en las URL

``` python
<img src="{% static "/fondo/foto.jpg" %}">
```

Tambien se puede itilizar la variable **STATICFILES_DIRS**

``` python
STATICFILES_DIRS = [
    Path.joinpath(BASE_DIR,'/core/notebook/static')
]
```

Para leer archivos **static** en cada **.html** es necesario incluir en el tope del fichero

``` html
{% load static %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Pagina Principal de Notas</title>
</head>
<body>
{% block container_notes %}
    <p>Container Vacio</p>
{% endblock %}
</body>
</html>
```






