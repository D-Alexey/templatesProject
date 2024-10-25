# Generated by Django 5.1.2 on 2024-10-24 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_base', '0023_alter_film_duration_alter_film_female_actor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='age',
            field=models.CharField(default='возраст', max_length=20),
        ),
        migrations.RemoveField(
            model_name='film',
            name='genres',
        ),
        migrations.AlterField(
            model_name='film',
            name='poster',
            field=models.CharField(default='постер', max_length=255, verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='film',
            name='title',
            field=models.CharField(default='тайтл', max_length=255, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='film',
            name='genres',
            field=models.CharField(default='женрес', max_length=255, verbose_name='Жанры'),
        ),
    ]
