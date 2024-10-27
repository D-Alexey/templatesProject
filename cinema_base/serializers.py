from contextlib import nullcontext

from django.template.defaultfilters import default
from rest_framework import serializers
from cinema_base import models


class Studio(serializers.ModelSerializer):
    class Meta:
        model = models.Studio
        fields = '__all__'

class Genre(serializers.ModelSerializer):
    class Meta:
        model = models.Genre
        fields = '__all__'

class Actor(serializers.ModelSerializer):
    class Meta:
        model = models.Actor
        fields = ['gender', 'first_name', 'surname', 'birth_date']

class Film(serializers.ModelSerializer):
    genres = Genre(many=True, read_only=True)
    male_actor = Actor['id']
    female_actor = Actor['id']
    studio = Studio['id']
    duration = serializers.DurationField(default='0')
    class Meta:
        model = models.Film
        fields = ['title', 'slogan', 'release', 'rating', 'age', 'male_actor', 'female_actor', 'studio', 'duration', 'genres', 'id']