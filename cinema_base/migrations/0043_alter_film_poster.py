# Generated by Django 5.1.2 on 2024-10-25 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_base', '0042_alter_film_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='poster',
            field=models.ImageField(default='./media/images/poster_none.jpg', upload_to='media/images'),
        ),
    ]
