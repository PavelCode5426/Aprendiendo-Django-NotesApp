# Generated by Django 4.0.4 on 2022-05-09 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'ordering': ['updated_at'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='note',
            name='titulo',
            field=models.CharField(default='Nueva Nota', max_length=255),
        ),
    ]
