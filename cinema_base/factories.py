import factory
from factory import Faker
from factory.django import ImageField

from cinema_base import models
from cinema_base.models import genders, ages
from faker import Faker
fake = Faker()
from django.utils import timezone
from datetime import timedelta, date, datetime
import random

class StudioFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('last_name')
    #name = 'Студия'
    class Meta:
        model = models.Studio

class GenreFactory(factory.django.DjangoModelFactory):
    name = factory.Faker('word')
    description = factory.Faker('text')
    class Meta:
        model = models.Genre

class ActorFactory(factory.django.DjangoModelFactory):
    photo = ImageField()
    first_name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    #birth_date = factory.Faker('birth_date')
    birth_date = factory.LazyFunction(lambda: fake.date_between(start_date='-10y', end_date='today'))
    gender = factory.Iterator(genders, getter=lambda arr: arr[0])
    #gender = 'male'
    #gender = genders[random.randint(0,1)]
    #print('actor birth date: ' + str(birth_date))
    class Meta:
        model = models.Actor

class FilmFactory(factory.django.DjangoModelFactory):
    title = 'тест тайтл'
    #poster = 'тест постер'
    poster = ImageField()
    #release = 'тест дата'
    release = factory.LazyFunction(lambda: fake.date_between(start_date='-50y', end_date='today'))
    #genres = 'тест жанры'
    #studio = 'тест студия'
    studio = factory.SubFactory(StudioFactory)
    #slogan = 'тест слоган'
    #male_actor = 'тест мужчина'
    male_actor = factory.SubFactory(ActorFactory)
    #female_actor = 'тест женщина'
    female_actor = factory.SubFactory(ActorFactory)
    #rating = 'тест рейтинг'
    rating = factory.Faker('pyint', min_value=0, max_value=100)
    #duration = 'тест дюрейшн'
    duration = factory.LazyFunction(lambda: timedelta(minutes=random.randint(0, 180)))
    #age = 'тест возраст'
    #age = ages[random.randint(0, len(ages) - 1)]
    age = factory.Iterator(ages, getter=lambda arr: arr[0])

    #title = factory.Faker('name')
    #poster = ImageField()
    #release = factory.Faker('release')
    #release = factory.LazyFunction(lambda: fake.date_between(start_date='-50y', end_date='today'))
    # genres = factory.SubFactory(GenreFactory)
    #studio = factory.SubFactory(StudioFactory)
    #slogan = factory.Faker('sentence')
    #male_actor = factory.SubFactory(ActorFactory)
    #female_actor = factory.SubFactory(ActorFactory)
    #rating = factory.Faker('pyint', min_value=0, max_value=100)
    #duration = factory.Faker('duration')
    #duration = factory.LazyFunction(lambda: timedelta(minutes=random.randint(0, 180)))
    #age = ages[random.randint(0, len(ages)-1)][0]

    @factory.post_generation
    def genres(self, create, extracted, **kwargs):
        print('работает пост генераатор')
        if not create:
            return

        if extracted:
            for genre in extracted:
                self.genres.add(genre)
        else:
            for i in range(0, random.randint(0,3)):
                self.genres.add(GenreFactory.create())

    class Meta:
        model = models.Film