from contextlib import nullcontext
from dataclasses import fields

from django.template.defaultfilters import default
from rest_framework import serializers
from rest_framework.fields import DateField

from cinema_base import models


class Professions(serializers.ModelSerializer):
    class Meta:
        model = models.Profession
        fields= '__all__'

class Studio(serializers.ModelSerializer):
    class Meta:
        model = models.Studio
        fields = '__all__'

class Genre(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'

class Person(serializers.ModelSerializer):
    professions = Professions(many=True, default=None)
    birth_date = DateField(default='1900-01-01')

    def create(self, validated_data):
        res = models.Actor.objects.create(
            gender=validated_data['gender'],
            first_name=validated_data['first_name'],
            surname=validated_data['surname'],
            birth_date=validated_data['birth_date']
        )
        if (validated_data['professions']):
            q = models.Profession.objects.filter(name__in=[profession['name'] for profession in validated_data['professions']])
            res.professions.set(q)
        return res

    class Meta:
        model = models.Person
        fields = ['gender', 'first_name', 'surname', 'professions', 'birth_date']

class Film(serializers.ModelSerializer):
    genres = Genre(many=True, default=None)
    directors = Person(many=True, default=None)
    male_actor = Person(default=None)
    female_actor = Person(default=None)
    studio = Studio(default=None)
    duration = serializers.DurationField(default='0')

    def create(self, validated_data):
        res = models.Person.objects.create(
            gender=validated_data['gender'],
            first_name=validated_data['first_name'],
            surname=validated_data['surname'],
            birth_date=validated_data['birth_date']
        )
        if (validated_data['genres']):
            q = models.Genre.objects.filter(
                name__in=[genre['name'] for genre in validated_data['genres']])
            res.genres.set(q)
        return res

    class Meta:
        model = models.Film
        fields = ['title', 'slogan', 'release', 'rating', 'age', 'directors', 'male_actor', 'female_actor', 'studio', 'duration', 'genres', 'id']