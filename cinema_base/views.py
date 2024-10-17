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

from cinema_base.models import Film

# Create your views here.
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
class FilmsList(ListView):
    template_name = 'cinema_base/films_list.html'
    model = Film
    #model = Film.objects.filter(male_actor__surname="Гослинг")
    #model = Film.objects.all()
    context_object_name = 'films'

class GoslingFilms(ListView):
    template_name = 'cinema_base/gosling_films.html'
    model = Film
    context_object_name = 'films'

class FilmDetail(DetailView):
    template_name = 'cinema_base/film_detail.html'
    model = Film
    context_object_name = 'film'

class FilmsUpdate(UpdateView):
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

    def get_success_url(self):
        return reverse_lazy('film_detail', kwargs={'pk': self.object.pk})

class FilmsDelete(DeleteView):
    model = Film
    template_name = 'cinema_base/film_confirm_delete.html'
    success_url = reverse_lazy('films_list')

class FilmCreate(CreateView):
    model = Film
    template_name = 'cinema_base/film_create.html'
    success_url = reverse_lazy('films_list')
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