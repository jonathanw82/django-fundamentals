# Generated by Django 3.0.5 on 2020-04-27 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='release',
            new_name='release_year',
        ),
    ]