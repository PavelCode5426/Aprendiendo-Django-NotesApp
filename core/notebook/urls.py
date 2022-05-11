from django.urls import path
from core.notebook.views import vista_basada_en_funcion, all_notes_template, NotesListView, NoteBooksListView, \
    NotesCreateView, NoteBookCreateView

#mismo nombre de variable que en config/urls.py
urlpatterns = [
    path('test',vista_basada_en_funcion),
    path('',all_notes_template,name='home'),

    #Utilizando ListView
    path('notes',NotesListView.as_view(),name='notes_list'),
    path('notes/add',NotesCreateView.as_view(),name='notes_create'),



    path('notebooks',NoteBooksListView.as_view(),name='notebook_list'),
    path('notebooks/add',NoteBookCreateView.as_view(),name='notebook_create')
]