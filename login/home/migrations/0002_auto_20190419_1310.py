# Generated by Django 2.2 on 2019-04-19 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='img',
            new_name='image',
        ),
    ]