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

## Vistas basadas en clases

Las vistas basadas en clases son una forma mas organizada de crear las vistas en nuestra aplicacion.

``` python
# Esta vista esta diseñada unicamente para listar contenido de un modelo, se le pasa la plantilla y se sobrescribe el metodo de get_context_data de forma que se actualicen los datos que se enviaran a la pantalla

class NotesListView(ListView):
    model = Note
    template_name = 'pages/notes_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Notas'
        #context['notes'] = context['object_list']
        return context

class NoteBooksListView(ListView):
    model = NoteBook
    template_name = 'pages/notebooks_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Libros de Notas'
        context['titleHead'] = 'Listado de Libros de Notas'
        #context['notebooks'] = context['object_list']
        return context
```

Tambien se puede editar el metodo get_query_set(self) el cual se utiliza para filtrar la consulta.

Tambien existe un metodo dispatch el cual recibe la paticion, puede resultar util en algun momento.

Es importante conocer que los metodos post en django estan protegidos por un token_csrf, dicho token esta activo porque se encuentra el middleware activado. En algunos casos es necesario dehabilitarlo, puede utilizarse el decorador **@csrf_exempt** cubriendo al metodo dispatch o al propio metodo post.


``` python
@method_decorator(csrf_exemp)
```

Uilizando los **CreateView**, es el mismo concepto que los list views, son una clase que contiene todo lo necesario para hacer vistar de insersion o modificacion de dato, por lo tanto agregan a sus datos un formulario. Estos formularios se crean hererando de la clase **ModelForm** (se puede crear un archivo form.py para contener los formularios si lo desea).

``` python
# form.py
from django.forms import ModelForm
from core.notebook.models import Note, NoteBook

class NotesForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        exclude = [] #Cuando trae valores x defecto o valores null
        
        
class NoteBookForm(ModelForm):
    class Meta:
        model = NoteBook
        fields = ['titulo']

# views.py
class NotesCreateView(CreateView):
    model = Note
    form_class = NotesForm
    template_name = 'components/container_new_note.html'
    success_url = reverse_lazy('notes_list') #Redireccionar cuando se haya enviado OK

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']=context['titleHead']='Creando Nueva Nota'
        return context

class NoteBookCreateView(CreateView):
    model = NoteBook
    form_class = NoteBookForm
    template_name = 'components/container_new_notebook.html'
    success_url = reverse_lazy('notebook_list') #Redireccionar cuando se haya enviado OK

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']=context['titleHead']='Creando Nueva Libreta'
        return context


# urls.py
path('notes/add',NotesCreateView.as_view(),name='notes_create')
path('notebooks/add',NoteBookCreateView.as_view()name='notebook_create')


#container_new_note.html
# Incleible como django crea el formulario con los tipos de datos.
{% block container %}
    <form method="post" action="/">
        {% csrf_token %}
        <div class="container-md row justify-content-center gap-2">
            {{ form }}
        </div>
    </form>
{% endblock %}

#Este formulario se puede modificar o mostrar de diferentes formas.
{{form.as_ul}} #Se muestra con componentes html <li></li>
{{form.as_table}} #Se muestra con componentes html <tr></tr>
{{form.as_p}} #Se muestra con componentes html <p></p>

# Accediendo a un determinado campo del Formulario
{{form.{campo}}}
{{form.{campo}.label}}
{{form.{campo}.value}}

```

Los **ModelForm** tambien se pueden modificar sus campos utilizando el atributo **widgets,labels** 

``` python
class NoteBookForm(ModelForm):
    class Meta:
        model = NoteBook
        fields = ['titulo']
        labels = {
            'titulo':'Titulo de Libreta'
        }

        widgets = {
            'titulo': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese un Titulo',
                'autocomplete': 'off'
            })
        }
   
#Cuando se busca hacer una unica vista para los formularios se puede hacer lo siguiente.

<div class="container-md row justify-content-center gap-2 mb-2">
            {% for field in form.visible_fields %}
                <div class="input-group">
                <label>{{ field.label }}</label>
                {{ field }}
                </div>
            {% endfor %}
        </div>


# Para evitar estar escribiendo lo mismo muchas veces...
widgets={
            'titulo': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese un Titulo',
                'autocomplete': 'off'
            }),
            'texto': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su nota',
                'autocomplete': 'off',
                'rows':'3'
            }),
            'tags': SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Seleccione sus Tags',
                'autocomplete': 'off'
            }),
            'notebook': Select(attrs={
                'class': 'form-control',
                'placeholder': 'Seleccione su libreta',
                'autocomplete': 'off'
            })
        }

# se puede sobreescribir el constructor quedando este resultado.
        class NotesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Individual
        self.fields['titulo'].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})

        # Para todos
        for form in self.visible_fields():
            # Forma 1
            form.field.widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})

            # Forma 2
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'

# Otra alternativa seria utilizar la libreria **widget_tweaks**
```

Existen mas tipos de views, por ejemplo el UpdateView, DeleteView, TemplateView, FormView ... pero se mantiene el concepto principal que es gestionar un modelo mediante una plantilla autogenerada.
* UpdateView: Crear una vista para actualizar el modelo.
* DeleteView: Crear una vista para borrar el modelo.
* TemplateView: Crear una pagina comun y corriente.
* FormView: Validar los datos del modelo, no hace mas nada. Mediante el uso del mismo se pueden crear validaciones personalizadas sobrescribiendo sus metodos.
* LoginView: Vista que permite crear el formulario de logueo, es otro Form, solo que este esta preparado para iniciar sesion.



## Validaciones de Formulario

Primero que todo los formularios que estan vinculados a un modelo se validan tal cual, si ocurre un error al insertar el modelo, actualizar o eliminar este volvera a la misma pagina con mensajes de error. Estos errores se capturan mediante el {{form.errors}}

Para validar el formulario
``` python 

# este codigo es opcional. Django lo hace automatico
class NoteBookCreateView(CreateView)
      def post(self, request, *args, **kwargs):
        #form = NoteBookForm(request.POST)
        form = self.get_form()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            self.object = None #Aqui se almacena el objeto que se crea, volverlo a poner en Null
            context= self.get_context_data(**kwargs)
            context['form'] = form
            return render(request,self.template_name,context)

# Si el formulario es invalido vuelve a cargar la misma pagina con los mismos datos y en caso contrario ve a otra url

#show_errors.html
{% if form.errors %}
    <ul class="card alert-danger">
        {% for error in form.errors.values %}
            {{ error }}
        {% endfor %}
    </ul>
{% endif %}

#in fields
{% for field in form.visible_fields %}
  <div class="form-group">
    <label class="fw-bolder" for="{{ field.name }}">{{ field.label }}</label>
     {{ field }}
    <label class="text-danger">{{ field.errors }}</label>
  </div>
{% endfor %}
```


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

# Decoradores en Django

Django utiliza decoradores para validar determinada informacion antes de ejecutar un metodo. 

``` python
# Para utilizar los decoradores de Django hay que importar la libreria.

from django.utils.decorators import method_decorator

@method_decorator(login_required)
@method_decorator(csrf_exemp)
def dispatch(.....):
    .......


```