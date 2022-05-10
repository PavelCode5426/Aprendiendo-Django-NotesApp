from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from core.notebook.models import Note, NoteBook


def vista_basada_en_funcion(request):
    return HttpResponse('Hola esta es mi primera URL')

def all_notes_template(request):
    data = {'notes': Note.objects.all(),'notebooks':NoteBook.objects.all()}
    #Se para el request, la direccion del html y la data (opcional)
    return render(request,'notes_list.html',data)