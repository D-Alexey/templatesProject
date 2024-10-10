# Generated by Django 5.1.2 on 2024-10-10 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_base', '0015_film_poster_film_release_alter_film_duration'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actor',
            options={'ordering': ['-surname'], 'verbose_name': 'Актёр', 'verbose_name_plural': 'Актёры'},
        ),
        migrations.AlterModelOptions(
            name='director',
            options={'ordering': ['-surname'], 'verbose_name': 'Режиссер', 'verbose_name_plural': 'Режиссеры'},
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ['-title'], 'verbose_name': 'Фильм', 'verbose_name_plural': 'Фильмы'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['-name'], 'verbose_name': 'Жанр', 'verbose_name_plural': 'Жанры'},
        ),
        migrations.AlterModelOptions(
            name='studio',
            options={'ordering': ['-name'], 'verbose_name': 'Студия', 'verbose_name_plural': 'Студии'},
        ),
    ]