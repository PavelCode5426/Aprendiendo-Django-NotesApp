from django.urls import path
from core.notebook.views import vista_basada_en_funcion, all_notes_template

#mismo nombre de variable que en config/urls.py
urlpatterns = [
    path('test',vista_basada_en_funcion),
    path('',all_notes_template)
]