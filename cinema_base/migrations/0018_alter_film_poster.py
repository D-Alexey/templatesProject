# Generated by Django 5.1.2 on 2024-10-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_base', '0017_actor_gender_alter_film_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='poster',
            field=models.ImageField(default='media/images/poster_none.jpg', upload_to='images'),
        ),
    ]