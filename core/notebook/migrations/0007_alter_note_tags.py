# Generated by Django 4.0.4 on 2022-05-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0006_alter_note_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(null=True, to='notebook.tag'),
        ),
    ]
