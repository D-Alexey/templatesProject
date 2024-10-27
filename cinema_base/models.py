from sys import maxsize
from tkinter.constants import CASCADE
from typing import reveal_type

from django.core.validators import MaxValueValidator

from django.db import models
from django.utils.version import version_component_re


# class Book(models.Model):
#     title = models.CharField(verbose_name='Название', max_length=255)
#     public_date = models.DateField(verbose_name='Дата публикации')
#     description = models.TextField(verbose_name='Описание' , blank=True)
#     author = models.ForeignKey(
#         'Author',
#         verbose_name='Автор',
#         blank=True,
#         null=True,
#         related_name='books',
#         on_delete=models.SET_NULL
#     )
#
#     class Meta:
#         verbose_name = 'Книга'
#         verbose_name_plural = 'Книги'
#         ordering = ['-title']
#
#     def __str__(self):
#         return self.title
#
# class Author(models.Model):
#     first_name = models.CharField('Имя', max_length=50)
#     surname = models.CharField('Фамилия', max_length=50)
#     patronymic = models.CharField('Отчество', max_length=50)
#     birth_date = models.DateField('Дата рождения')
#
#     class Meta:
#         verbose_name = 'Автор'
#         verbose_name_plural = 'Авторы'
#         ordering = ['-first_name']
#
#     def __str__(self):
#         return f'{self.first_name} {self.surname} {self.patronymic}'
#
# class Genre(models.Model):
#     name = models.CharField('Название', max_length=50)
#     description = models.TextField(verbose_name='Описание', blank=True)
#     books = models.ManyToManyField(
#         Book,
#         verbose_name='Книги',
#         related_name='genres',
#         blank=True,
#         null=True
#     )
#
#     class Meta:
#         verbose_name = 'Жанр'
#         verbose_name_plural = 'Жанры'
#         ordering = ['-name']
#
#     def __str__(self):
#         return self.name
#
# class Storage(models.Model):
#     amount = models.PositiveIntegerField('Количество')
#     price = models.PositiveIntegerField('Цена')
#     book = models.OneToOneField(
#         Book,
#         on_delete=models.CASCADE,
#         blank=True,
#         null=True,
#         related_name='storage',
#         verbose_name='Книга'
#     )
#
#     # class Meta:
#     #     verbose_name = 'Склад'
#     #     verbose_name_plural = 'Склады'
#     #     ordering = ['amount, price']
#
#     def __str__(self):
#         return f'{self.book} - {self.price}'
#
#     def get_discount(self):
#         return self.price - (self.price * 0.1)

#import modelsProject; from cinema_base.models import *; from datetime import timedelta

genders = [
    ('male', 'male'),
    ('female', 'female')
]

ages = [
    ('G', 'General Audiences'),
    ('PG', 'Parental Guldence Suggested'),
    ('PG', 'Parental Guldence Suggested'),
    ('PG-13', 'Parents Strongly Caoutioned'),
    ('R', 'Restricted'),
    ('NC-17', 'Adults Only'),
    ('NONE', 'None Information')
]

class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=255)
    description = models.TextField(verbose_name='Описание', blank=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
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

class Actor(models.Model):
    photo = models.ImageField(upload_to='media/images/peoples', default='/media/images/poster_none.jpg')
    first_name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    birth_date = models.DateField('Дата рождения', default='1900-01-01')
    gender = models.CharField(max_length=6, choices=genders, default='None')
    #gender = models.CharField(max_length=6, default='None')

    class Meta:
        verbose_name = 'Актёр'
        verbose_name_plural = 'Актёры'
        ordering = ['-surname']

    def __str__(self):
        return f'{self.first_name} {self.surname}' #{self.patronymic}'

    def getinfo(self):
        return f'{self.first_name} {self.surname}, {self.gender}'

class Film(models.Model):
    title = models.CharField(verbose_name='Название', max_length=255)
    poster = models.ImageField(upload_to='media/images', default='/media/images/poster_none.jpg')
    #poster = models.CharField(verbose_name='Постер', max_length=255, default='постер')
    release = models.DateField('Дата выхода', default='1900-01-01')
    #release = models.CharField(verbose_name='Постер', max_length=255, default='дата')
    genres = models.ManyToManyField(Genre, verbose_name='Жанры', related_name='films', blank=True, null=True)
    #genres = models.CharField(verbose_name='Жанры', max_length=255, default='женрес')
    studio = models.ForeignKey(Studio, verbose_name='Студия', blank=True, null=True, related_name='studio', on_delete=models.SET_NULL)
    #studio = models.CharField(verbose_name='Студия', max_length=255, default='студия')
    slogan = models.CharField(verbose_name='Слоган', max_length=255, blank=True, default='')
    male_actor = models.ForeignKey(Actor, on_delete=models.SET_NULL, related_name='male_actor', blank=True, null=True)
    #male_actor = models.CharField(verbose_name='Мужская роль', max_length=255, default='мэйл')
    female_actor = models.ForeignKey(Actor, on_delete=models.SET_NULL, related_name='female_actor', blank=True, null=True)
    #female_actor = models.CharField(verbose_name='Женская роль', max_length=255, default='фемэйл')
    rating = models.PositiveIntegerField(verbose_name='Оценка', validators=[MaxValueValidator(100)], default=0)
    #rating = models.CharField(verbose_name='Рейтинг', max_length=255, default='рейтинг')
    duration = models.DurationField(verbose_name='Длительность', blank=True, default='00:00:00')
    #duration = models.CharField(verbose_name='Длительность', max_length=255, default='длительность')
    #age = models.CharField(max_length=20, default='возраст')
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
        # return  (*self.genres.all())
        #return 'Функция гетженрес'
        return ', '.join(self.genres.values_list('name', flat=True))

    def getinfo(self):
        return (f'\nНазвание: {self.title:<20} Дата выхода: {str(self.release):<20} Жанры: {self.getgenres():<20} '
                f'\nСлоган: {str(self.slogan):<100} \nСтудия: {str(self.studio):<20} '
                f'\nГлавные актёры: {str(self.male_actor):<20} {str(self.female_actor):<20} '
                f'\nОценка: {self.rating:<20} Длительность: {str(self.duration):<20} Рейтинг: {self.age:<20} \n')

class Director(models.Model):
    first_name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    birth_date = models.DateField('Дата рождения')
    films = models.ManyToManyField(Film, verbose_name='Фильм', related_name='films', blank=True)

    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'
        ordering = ['-surname']

    def __str__(self):
        return f'{self.first_name} {self.surname}' #{self.patronymic}'