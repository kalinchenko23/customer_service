# Generated by Django 3.1.1 on 2020-09-26 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200920_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='pdf',
            field=models.FileField(blank=True, upload_to='profile_pdf'),
        ),
    ]
