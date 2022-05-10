from django.contrib import admin

# Register your models here.
from core.notebook.models import *

admin.site.register(Tag)
admin.site.register(NoteBook)
admin.site.register(Note)
