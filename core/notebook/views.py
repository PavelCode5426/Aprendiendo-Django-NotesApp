from multiprocessing import get_context

from django.http import HttpResponse
from django.shortcuts import render

from django.views.generic import ListView
# Create your views here.

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
