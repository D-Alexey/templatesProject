# Generated by Django 5.1.2 on 2024-11-06 17:08

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
            ],
            options={
                'verbose_name': 'Режиссер',
                'verbose_name_plural': 'Режиссеры',
                'ordering': ['-surname'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Жанр')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Профессия')),
            ],
            options={
                'verbose_name': 'Профессия',
                'verbose_name_plural': 'Профессии',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Студия')),
            ],
            options={
                'verbose_name': 'Студия',
                'verbose_name_plural': 'Студии',
                'ordering': ['-name'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('photo', models.ImageField(default='/media/images/avatars/default_avatar.jpg', upload_to='media/images/avatars', verbose_name='Фото')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='/media/images/poster_none.jpg', upload_to='media/images/peoples', verbose_name='Фото')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('birth_date', models.DateField(default='1900-01-01', verbose_name='Дата рождения')),
                ('gender', models.CharField(choices=[('male', 'М'), ('female', 'Ж')], default='None', max_length=6, verbose_name='Пол')),
                ('professions', models.ManyToManyField(blank=True, default=None, null=True, related_name='actors', to='cinema_base.profession', verbose_name='Профессия')),
            ],
            options={
                'verbose_name': 'Актёр',
                'verbose_name_plural': 'Актёры',
                'ordering': ['-surname'],
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('poster', models.ImageField(default='/media/images/poster_none.jpg', upload_to='media/images')),
                ('release', models.DateField(default='1900-01-01', verbose_name='Дата выхода')),
                ('slogan', models.CharField(blank=True, default='', max_length=255, verbose_name='Слоган')),
                ('rating', models.PositiveIntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100)], verbose_name='Оценка')),
                ('duration', models.DurationField(blank=True, default='00:00:00', verbose_name='Длительность')),
                ('age', models.CharField(choices=[('G', 'Нет возрастных ограничений'), ('PG', 'Рекомендуется присутствие родителей'), ('PG-13', 'Детям до 13 лет просмотр не желателен'), ('R', 'Лицам до 17 лет обязательно присутствие взрослого'), ('NC-17', 'Лицам до 18 лет просмотр запрещен'), ('NONE', 'Неизвестно')], default='None', max_length=5)),
                ('directors', models.ManyToManyField(blank=True, default=None, limit_choices_to={'professions__name': 'Режиссёр'}, related_name='directors', to='cinema_base.actor', verbose_name='Режиссер')),
                ('female_actor', models.ForeignKey(blank=True, limit_choices_to={'gender': 'female', 'professions__name': 'Актёр'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='female_actor', to='cinema_base.actor')),
                ('male_actor', models.ForeignKey(blank=True, limit_choices_to={'gender': 'male', 'professions__name': 'Актёр'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='male_actor', to='cinema_base.actor')),
                ('genres', models.ManyToManyField(blank=True, default=None, null=True, related_name='films', to='cinema_base.genre', verbose_name='Жанры')),
                ('studio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='studio', to='cinema_base.studio', verbose_name='Студия')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
                'ordering': ['-title'],
            },
        ),
    ]
