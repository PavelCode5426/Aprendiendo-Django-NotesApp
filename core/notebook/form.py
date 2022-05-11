from django.forms import ModelForm, TextInput, Textarea, SelectMultiple, Select

from core.notebook.models import Note, NoteBook


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


    class Meta:
        model = Note
        fields = '__all__'
        exclude = [] #Cuando trae valores x defecto o valores null

        widgets={

            'titulo': TextInput(attrs={
                'placeholder': 'Ingrese un Titulo',
            }),
            'texto': Textarea(attrs={
                'placeholder': 'Ingrese su nota',
                'rows':'3'
            }),
            'tags': SelectMultiple(attrs={
                'placeholder': 'Seleccione sus Tags',
            }),
            'notebook': Select(attrs={
                'placeholder': 'Seleccione su libreta',
            })
        }


class NoteBookForm(ModelForm):
    class Meta:
        model = NoteBook
        fields = ['titulo']

        labels = {'titulo':'Titulo de Libreta'}

        widgets = {
            'titulo': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese un Titulo',
                'autocomplete': 'off'
            })
        }