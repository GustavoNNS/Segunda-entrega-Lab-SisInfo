# Generated by Django 5.1.3 on 2024-11-15 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogoFotos', '0002_rename_post_posts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Posts',
            new_name='Post',
        ),
    ]