# Generated by Django 3.0.2 on 2020-10-13 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='gallery_image',
            new_name='image',
        ),
    ]
