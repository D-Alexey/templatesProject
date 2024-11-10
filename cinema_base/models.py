from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator

from django.db import models

#import modelsProject; from cinema_base.models import *; from datetime import timedelta

genders = [
    ('male', 'М'),
    ('female', 'Ж')
]

ages = [
    ('G', 'Нет возрастных ограничений'),
    ('PG', 'Рекомендуется присутствие родителей'),
    ('PG-13', 'Детям до 13 лет просмотр не желателен'),
    ('R', 'Лицам до 17 лет обязательно присутствие взрослого'),
    ('NC-17', 'Лицам до 18 лет просмотр запрещен'),
    ('NONE', 'Неизвестно')
]

class User(AbstractUser):
    photo = models.ImageField('Фото', upload_to='media/images/avatars', blank=True, null=True)#default='/media/images/avatars/default_avatar.jpg')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

class UsersNotes(models.Model):
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    film = models.ForeignKey('Film', verbose_name='Фильм', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(verbose_name='Оценка', validators=[MaxValueValidator(100)], default=0)
    note = models.TextField(verbose_name='Описание', blank=True)

class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['-name']

    def __str__(self):
        return self.name

class Profession(models.Model):
    name = models.CharField(verbose_name='Профессия', max_length=255)

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'
        ordering = ['-name']

    def __str__(self):
        return self.name

class Studio(models.Model):
    name = models.CharField(verbose_name='Студия', max_length=255, unique=True)

    class Meta:
        verbose_name = 'Студия'
        verbose_name_plural = 'Студии'
        ordering = ['-name']

    def __str__(self):
        return self.name

class Person(models.Model):
    photo = models.ImageField('Фото', upload_to='media/images/peoples', blank=True, null=True)
    first_name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    birth_date = models.DateField('Дата рождения', default='1900-01-01')
    gender = models.CharField('Пол', max_length=6, choices=genders, default='None')
    professions = models.ManyToManyField(Profession, verbose_name='Профессия', related_name='Persons', blank=True, default=None)

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['-surname']

    def __str__(self):
        return f'{self.first_name} {self.surname}'

    def getinfo(self):
        return f'{self.first_name} {self.surname}, {self.gender}, {self.getprofessions()}'

    def getprofessions(self):
        return ', '.join(self.professions.values_list('name', flat=True))

class Film(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    poster = models.ImageField(upload_to='media/images/posters', blank=True, null=True)
    directors = models.ManyToManyField(Person, verbose_name='Режиссер', related_name='directors', blank=True, limit_choices_to = {"professions__name": "Режиссёр"}, default=None)
    release = models.DateField('Дата выхода', default='1900-01-01')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры', related_name='films', blank=True, default=None)
    studio = models.ForeignKey(Studio, verbose_name='Студия', blank=True, null=True, related_name='studio', on_delete=models.SET_NULL)
    slogan = models.CharField(verbose_name='Слоган', max_length=255, blank=True, default='')
    male_actor = models.ForeignKey(Person, on_delete=models.SET_NULL, related_name='male_actor', blank=True, null=True, limit_choices_to = {"professions__name": "Актёр","gender": "male"})

    female_actor = models.ForeignKey(Person, on_delete=models.SET_NULL, related_name='female_actor', blank=True, null=True, limit_choices_to = {"professions__name": "Актёр","gender": "female"})
    rating = models.PositiveIntegerField(verbose_name='Оценка', validators=[MaxValueValidator(100)], default=0)
    duration = models.DurationField(verbose_name='Длительность', blank=True, default='00:00:00')
    age = models.CharField(
        max_length=5,
        choices=ages,
        default='None',
    )

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['-title']

    def __str__(self):
        return self.title

    def rating100to10(self):
        return f'rate new: {round(self.rating / 10, 1)}'

    def rating100to5(self):
        return self.rating // 25

    def getgenres(self):
        return ', '.join(self.genres.values_list('name', flat=True))

    def getdirectors(self):
        return [x[0] for x in self.directors.values_list('pk')]

    def getinfo(self):
        return (f'\nНазвание: {self.title:<20} Дата выхода: {str(self.release):<20} Жанры: {self.getgenres():<20} '
                f'\nСлоган: {str(self.slogan):<100} \nСтудия: {str(self.studio):<20} '
                f'\nГлавные актёры: {str(self.male_actor):<20} {str(self.female_actor):<20} '
                f'\nОценка: {self.rating:<20} Длительность: {str(self.duration):<20} Рейтинг: {self.age:<20} \n')