# Generated by Django 4.0.4 on 2022-05-11 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0005_alter_notebook_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='titulo',
            field=models.CharField(default='Nueva Nota', max_length=255, unique=True),
        ),
    ]