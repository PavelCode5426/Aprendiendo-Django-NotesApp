# Generated by Django 4.0.4 on 2022-05-09 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0003_note_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('titulo', models.CharField(default='Nuevo Libro de Notas', max_length=250)),
            ],
            options={
                'ordering': ['updated_at'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='note',
            name='notebook',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='notebook.notebook'),
        ),
    ]