# Generated by Django 3.2.18 on 2023-04-27 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('linea', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('NS', models.CharField(help_text='Numero de serie del producto', max_length=20)),
                ('existencias', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='PlacasBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('linea', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('NS', models.CharField(help_text='Numero de serie del producto', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Procesadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=20)),
                ('linea', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('NS', models.CharField(help_text='Numero de serie del producto', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SwPropietario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RFC', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=30)),
                ('apPaterno', models.CharField(max_length=30)),
                ('apMaterno', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('calle', models.CharField(max_length=50)),
                ('colonia', models.CharField(max_length=40)),
                ('municipio', models.CharField(max_length=40)),
                ('numeroContacto', models.CharField(max_length=40)),
                ('CP', models.CharField(max_length=5)),
                ('edad', models.IntegerField(default=0)),
                ('descripcion', models.CharField(max_length=30)),
                ('presupuesto', models.CharField(max_length=100)),
            ],
        ),
    ]