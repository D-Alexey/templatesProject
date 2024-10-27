from lib2to3.fixes.fix_input import context
from platform import release

# from msilib.schema import ListView

from django.shortcuts import render
from django.http import HttpResponse
from django.template.base import kwarg_re
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView, ListView, CreateView
from django.core.files.storage import FileSystemStorage
from django_filters.views import FilterView
from django.db.models import Q
from rest_framework import viewsets

from cinema_base.models import Film, Studio, Actor, Genre
from cinema_base import filters
from cinema_base import serializers

class GenreAPI(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.Genre

class ActorAPI(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = serializers.Actor

class StudioAPI(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = serializers.Studio

class FilmAPI(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = serializers.Film

class FirstView(View):
    def get(self, request):
        return HttpResponse('Привет джанго')

# class FilmsListTemplateView(TemplateView):
#     template_name = 'cinema_base/films_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['films'] = Film.objects.all()
#         return context
# 11 08 - views class List
# class FilmsList(ListView):
#     template_name = 'cinema_base/films_list.html'
#     model = Film
#     context_object_name = 'films'

class FilmsList(FilterView):
    template_name = 'cinema_base/films_list.html'
    model = Film
    context_object_name = 'films'
    filterset_class = filters.Film

class GoslingFilms(ListView):
    template_name = 'cinema_base/gosling_films.html'
    model = Film
    context_object_name = 'films'

class FilmDetail(DetailView):
    template_name = 'cinema_base/film_detail.html'
    model = Film
    context_object_name = 'film'

class FilmsUpdate(UpdateView):
    def __init__(self):
        super().__init__()
        print('фильм апдейт')
    model = Film
    template_name = 'cinema_base/film_form.html'
    fields = ['title',
              'release',
              'slogan',
              'genres',
              'studio',
              'slogan',
              'male_actor',
              'female_actor',
              'rating',
              'duration',
              'age',
              'poster']
    success_url = reverse_lazy('films_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('film_detail', kwargs={'pk': self.object.pk})

class FilmsDelete(DeleteView):
    model = Film
    template_name = 'cinema_base/film_confirm_delete.html'
    success_url = reverse_lazy('films_list')

class FilmCreate(CreateView):
    def __init__(self):
        super().__init__()
    model = Film
    template_name = 'cinema_base/film_create.html'
    success_url = reverse_lazy('films_list')
    fields = ['title',
              'release',
              'slogan',
              'genres',
              'studio',
              'male_actor',
              'female_actor',
              'rating',
              'duration',
              'age',
              'poster']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('films_list')

class ActorsList(FilterView):
    template_name = 'cinema_base/actors_list.html'
    model = Actor
    context_object_name = 'actors'
    filterset_class = filters.Actor

class ActorDetail(DetailView):
    template_name = 'cinema_base/actor_detail.html'
    model = Actor
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['films'] = Film.objects.filter(Q(female_actor__id=self.object.pk) | Q(male_actor__id=self.object.pk))
        print(self.object.pk)
        return context

class ActorCreate(CreateView):
    model = Actor
    template_name = 'cinema_base/actor_create.html'
    success_url = reverse_lazy('actors_list')
    fields = [
        'photo',
        'first_name',
        'surname',
        'birth_date',
        'gender'
    ]

class ActorUpdate(UpdateView):
    model = Actor
    template_name = 'cinema_base/actor_form.html'
    fields = [
        'photo',
        'first_name',
        'surname',
        'birth_date',
        'gender'
    ]
    success_url = reverse_lazy('actors_list')

class ActorDelete(DeleteView):
    model = Actor
    template_name = 'cinema_base/actor_confirm_delete.html'
    success_url = reverse_lazy('actors_list')
