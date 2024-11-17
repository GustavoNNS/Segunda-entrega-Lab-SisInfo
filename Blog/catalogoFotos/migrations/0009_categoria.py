# Generated by Django 5.1.3 on 2024-11-17 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogoFotos', '0008_comentario_data_postagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao', models.CharField(max_length=255)),
                ('fotos', models.ManyToManyField(to='catalogoFotos.post')),
            ],
        ),
    ]