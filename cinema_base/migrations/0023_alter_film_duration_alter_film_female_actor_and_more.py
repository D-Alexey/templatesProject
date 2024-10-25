# Generated by Django 5.1.2 on 2024-10-24 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_base', '0022_alter_film_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='duration',
            field=models.DurationField(blank=True, null=True, verbose_name='Длительность'),
        ),
        migrations.AlterField(
            model_name='film',
            name='female_actor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='female_actor', to='cinema_base.actor'),
        ),
        migrations.AlterField(
            model_name='film',
            name='genres',
            field=models.ManyToManyField(blank=True, related_name='films', to='cinema_base.genre', verbose_name='Жанры'),
        ),
        migrations.AlterField(
            model_name='film',
            name='male_actor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='male_actor', to='cinema_base.actor'),
        ),
        migrations.AlterField(
            model_name='film',
            name='slogan',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Слоган'),
        ),
        migrations.AlterField(
            model_name='film',
            name='studio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='studio', to='cinema_base.studio', verbose_name='Студия'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]
