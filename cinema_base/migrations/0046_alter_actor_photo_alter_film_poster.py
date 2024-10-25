# Generated by Django 5.1.2 on 2024-10-25 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_base', '0045_alter_actor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='photo',
            field=models.ImageField(default='/media/images/poster_none.jpg', upload_to='media/images/peoples'),
        ),
        migrations.AlterField(
            model_name='film',
            name='poster',
            field=models.ImageField(default='/media/images/poster_none.jpg', upload_to='media/images'),
        ),
    ]
