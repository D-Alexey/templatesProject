# Generated by Django 5.1.2 on 2024-10-10 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_base', '0012_film_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='duration',
            field=models.IntegerField(blank=True, default=0, verbose_name='Длительность'),
        ),
    ]