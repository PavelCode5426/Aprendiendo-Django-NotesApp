# Generated by Django 4.0.4 on 2022-05-09 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0002_tag_alter_note_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(to='notebook.tag'),
        ),
    ]