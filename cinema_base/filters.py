from random import choice

import django_filters
from django.forms import ChoiceField

import cinema_base.models
from django.db.models import Q
from cinema_base.models import Genre, ages, genders
from datetime import datetime, date, time

QUALITY = [
    ('Hight_rating', 'Высокая'),
    ('Average_rating', 'Средняя'),
    ('Low_rating', 'Низкая')
]

class Person(django_filters.FilterSet):
    #person = django_filters.CharFilter(method='actor_filter', label='Актер')
    first_name = django_filters.CharFilter(lookup_expr='iregex', label='Имя')
    surname = django_filters.CharFilter(lookup_expr='iregex', label='Фамилия')
    year = django_filters.RangeFilter(field_name='birth_date__year', label='Год рождения от и до')
    gender = django_filters.ChoiceFilter(choices=genders, field_name='gender', label='Пол')

class Film(django_filters.FilterSet):
    rating_range = django_filters.RangeFilter(field_name='rating', label='Рейтинг от и до')
    title = django_filters.CharFilter(lookup_expr='iregex', label='Название', )
    slogan = django_filters.CharFilter(lookup_expr='iregex', label='Слоган', )
    actor = django_filters.CharFilter(method='actor_filter', label='Актер')
    age_rating = django_filters.MultipleChoiceFilter(choices=ages, field_name='age', label='Возрастной рейтинг')
    genres = django_filters.ModelMultipleChoiceFilter(queryset=Genre.objects.all(), method='genre_filter', field_name='genres__name', label='Жанры')
    rating = django_filters.ChoiceFilter(choices=QUALITY, method='rating_filter', label='Оценка')
    year = django_filters.RangeFilter(field_name='release__year', label='Год от и до')

    class Meta:
        model = cinema_base.models.Film
        fields = ['title', 'slogan', 'actor', 'genres', 'age_rating', 'rating', 'year']

    def rating_filter(self, queryset, name, value):
        if value == QUALITY[0][0]:
             return queryset.filter(rating__gt=66)
        if value == QUALITY[1][0]:
             return queryset.filter(rating__lt=66, rating__gt=33)
        if value == QUALITY[2][0]:
             return queryset.filter(rating__lt=33)
        return queryset

    def genre_filter(self, queryset, name, value):
        for gener in value:
            queryset = queryset.filter(genres=gener)
        return queryset

    def actor_filter(self, queryset, name, value):
        crit = Q()
        for term in value.split():
            crit &= Q(male_actor__surname__iregex=term) | Q(female_actor__surname__iregex=term) | Q(male_actor__first_name__iregex=term) | Q(female_actor__first_name__iregex=term)
        return queryset.filter(crit).distinct()