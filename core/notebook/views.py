
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, UpdateView
# Create your views here.
from core.notebook.form import NotesForm, NoteBookForm
from core.notebook.models import Note, NoteBook


def vista_basada_en_funcion(request):
    return HttpResponse('Hola esta es mi primera URL')

def all_notes_template(request):
    data = {'notes': Note.objects.all(),'notebooks':NoteBook.objects.all()}
    #Se para el request, la direccion del html y la data (opcional)
    return render(request, 'notes_notebooks_list.html', data)


# VISTAS BASADAS EN CLASES
class NotesListView(ListView):
    model = Note
    template_name = 'pages/notes_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Notas'
        context['titleHead'] = 'Listado de Notas'
        context['notes'] = context['object_list']
        return context
class NoteBooksListView(ListView):
    model = NoteBook
    template_name = 'pages/notebooks_list.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Libros de Notas'
        context['titleHead'] = 'Listado de Libros de Notas'
        context['notebooks'] = context['object_list']
        return context


class NotesCreateView(CreateView):
    model = Note
    form_class = NotesForm
    template_name = 'components/container_new_all.html'
    success_url = reverse_lazy('notes_list') #Redireccionar cuando se haya enviado OK


    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']=context['titleHead']='Creando Nueva Nota'
        context['cancel_url']= reverse_lazy('notes_list')
        return context
class NoteBookCreateView(CreateView):
    model = NoteBook
    form_class = NoteBookForm
    template_name = 'components/container_new_all.html'
    success_url = reverse_lazy('notebook_list') #Redireccionar cuando se haya enviado OK

    def post(self, request, *args, **kwargs):
        response=None
        #form = NoteBookForm(request.POST)
        form = self.get_form()
        if form.is_valid():
            form.save()
            response=HttpResponseRedirect(self.success_url)
        else:
            self.object = None #Aqui se almacena el objeto que se crea, volverlo a poner en Null
            context= self.get_context_data(**kwargs)
            context['form'] = form
            response=render(request,self.template_name,context)
        return response

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']=context['titleHead']='Creando Nueva Libreta'
        context['cancel_url'] = reverse_lazy('notebook_list')
        return context


class NotesUpdateView(UpdateView):
    model = Note
    form_class = NotesForm
    template_name = 'components/container_new_all.html'
    success_url = reverse_lazy('notes_list')  # Redireccionar cuando se haya enviado OK

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['titleHead'] = 'Editando Nota'
        context['cancel_url'] = reverse_lazy('notes_list')
        return context

