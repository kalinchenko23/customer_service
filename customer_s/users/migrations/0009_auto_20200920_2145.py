# Generated by Django 3.1.1 on 2020-09-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20200920_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rank',
            field=models.CharField(blank=True, max_length=3),
        ),
    ]
