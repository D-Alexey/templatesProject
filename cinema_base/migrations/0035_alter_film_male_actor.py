# Generated by Django 5.1.2 on 2024-10-24 22:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_base', '0034_alter_film_studio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='male_actor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='male_actor', to='cinema_base.actor'),
        ),
    ]
