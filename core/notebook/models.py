from django.db import models

# Create your models here.
class HasTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True #Para heredar de la clase de forma abstracta
        ordering = ['updated_at']

class Tag(HasTimeStamp):
    name = models.CharField(max_length=255,unique=True)

    def __str__(self):
        return self.name

class NoteBook(HasTimeStamp):
    titulo = models.CharField(max_length=250,default='Nuevo Libro de Notas')

    def __str__(self):
        return self.titulo

class Note(HasTimeStamp):
    titulo = models.CharField(max_length=255,default='Nueva Nota')
    texto = models.TextField(blank=True)
    tags = models.ManyToManyField(Tag)
    notebook = models.ForeignKey(NoteBook,on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.titulo