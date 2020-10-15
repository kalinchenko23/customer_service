# Generated by Django 3.1.1 on 2020-09-26 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0014_auto_20200926_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acft',
            name='dead_lift',
            field=models.CharField(blank=True, choices=[(140, 140), (150, 150), (160, 160), (170, 170), (180, 180), (190, 190), (200, 200), (210, 210), (220, 220), (230, 230), (240, 240), (250, 250), (260, 260), (270, 270), (280, 280), (290, 290), (300, 300), (310, 310), (320, 320), (330, 330), (340, 340)], max_length=3),
        ),
        migrations.AlterField(
            model_name='acft',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='acft',
            name='pushups',
            field=models.CharField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31), (32, 32), (33, 33), (34, 34), (35, 35), (36, 36), (37, 37), (38, 38), (39, 39), (40, 40), (41, 41), (42, 42), (43, 43), (44, 44), (45, 45), (46, 46), (47, 47), (48, 48), (49, 49), (50, 50), (51, 51), (52, 52), (53, 53), (54, 54), (55, 55), (56, 56), (57, 57), (58, 58), (59, 59), (60, 60)], max_length=2),
        ),
    ]