# Generated by Django 3.1.1 on 2020-09-15 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='pdf',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='title',
        ),
    ]
