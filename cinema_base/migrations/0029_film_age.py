# Generated by Django 5.1.2 on 2024-10-24 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_base', '0028_remove_film_age_alter_film_duration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='age',
            field=models.CharField(default='возраст', max_length=20),
        ),
    ]