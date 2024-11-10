from django.contrib.auth import logout, login, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView

from django.shortcuts import redirect
from django.http import HttpResponse
from django.template.base import kwarg_re
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, DetailView, UpdateView, DeleteView, ListView, CreateView, FormView
from django.core.files.storage import FileSystemStorage
from django_filters.views import FilterView
from django.db.models import Q
from rest_framework import viewsets

from cinema_base.forms import RegisterUserForm, NoteForm
from cinema_base.models import Film, Studio, Person, Genre, UsersNotes, User
from cinema_base import filters
from cinema_base import serializers
from modelsProject import settings


class GenreAPI(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = serializers.Genre

class PersonAPI(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = serializers.Person

class StudioAPI(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = serializers.Studio

class FilmAPI(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = serializers.Film

class FirstView(View):
    def get(self, request):
        return HttpResponse('Привет джанго')

class FilmsList(FilterView):
    template_name = 'cinema_base/films_list.html'
    model = Film
    context_object_name = 'films'
    filterset_class = filters.Film
    extra_context = {
        'default_image': settings.DEFAULT_POSTER_IMAGE,
    }

class FilmCreate(CreateView):
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
              'directors',
              'rating',
              'duration',
              'age',
              'poster']

    def get_success_url(self):
        return reverse_lazy('films_list')

class FilmDetail(DetailView):
    template_name = 'cinema_base/film_detail.html'
    model = Film
    context_object_name = 'film'
    extra_context = {
        'default_image': settings.DEFAULT_POSTER_IMAGE,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = UsersNotes.objects.filter(film_id=context['object'].pk)
        context['users'] = User.objects.filter(pk__in=[x[0] for x in context['notes'].values_list('user_id')])
        return context

class FilmsUpdate(UpdateView):
    model = Film
    template_name = 'cinema_base/film_form.html'
    fields = ['title',
              'release',
              'slogan',
              'genres',
              'studio',
              'slogan',
              'directors',
              'male_actor',
              'female_actor',
              'rating',
              'duration',
              'age',
              'poster']
    success_url = reverse_lazy('films_list')
    extra_context = {
        'default_image': settings.DEFAULT_POSTER_IMAGE,
    }

    def get_success_url(self):
        return reverse_lazy('film_detail', kwargs={'pk': self.object.pk})

class FilmsDelete(DeleteView):
    model = Film
    template_name = 'cinema_base/film_confirm_delete.html'
    success_url = reverse_lazy('films_list')

class ActorsList(FilterView):
    template_name = 'cinema_base/actors_list.html'
    model = Person
    context_object_name = 'persons'
    filterset_class = filters.Person
    extra_context = {
        'default_image': settings.DEFAULT_POSTER_IMAGE,
    }
    def get_queryset(self):
        return Person.objects.all().filter(professions__name='Актёр')

class DirectorsList(FilterView):
    template_name = 'cinema_base/directors_list.html'
    model = Person
    context_object_name = 'persons'
    filterset_class = filters.Person
    extra_context = {
        'default_image': settings.DEFAULT_POSTER_IMAGE,
    }
    def get_queryset(self):
        return Person.objects.all().filter(professions__name='Режиссёр')

class PersonCreate(CreateView):
    model = Person
    template_name = 'cinema_base/person_create.html'
    success_url = reverse_lazy('films_list')
    fields = [
        'photo',
        'first_name',
        'surname',
        'birth_date',
        'professions',
        'gender'
    ]

class PersonDetail(DetailView):
    template_name = 'cinema_base/person_detail.html'
    model = Person
    extra_context = {
        'default_image': settings.DEFAULT_POSTER_IMAGE,
    }
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['films'] = Film.objects.filter(Q(female_actor__id=self.object.pk) | Q(male_actor__id=self.object.pk) | Q(directors__pk=self.object.pk))
        return context

class PersonUpdate(UpdateView):
    model = Person
    template_name = 'cinema_base/person_form.html'
    fields = [
        'photo',
        'first_name',
        'surname',
        'birth_date',
        'professions',
        'gender'
    ]
    extra_context = {
        'default_image': settings.DEFAULT_POSTER_IMAGE,
    }
    success_url = reverse_lazy('films_list')

class PersonDelete(DeleteView):
    model = Person
    template_name = 'cinema_base/person_confirm_delete.html'
    success_url = reverse_lazy('films_list')

class NoteCreate(CreateView):
    model = UsersNotes
    template_name = 'cinema_base/note_create.html'
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.user_id = self.request.user.pk
        form.instance.film_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('films_list')

class NoteUpdate(UpdateView):
    model = UsersNotes
    form_class = NoteForm
    template_name = 'cinema_base/note_update.html'

    def get_success_url(self):
        return reverse_lazy('films_list')

class NoteDelete(DeleteView):
    model = UsersNotes
    template_name = 'cinema_base/note_delete.html'
    success_url = reverse_lazy('films_list')

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'cinema_base/register.html'
    success_url = reverse_lazy('films_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('films_list')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'cinema_base/login.html'

    def get_success_url(self):
        return reverse_lazy('films_list')

def logout_user(request):
    logout(request)
    return redirect('login')

class ProfileUser(UpdateView):
    model = get_user_model()
    fields = [
        'photo',
        'username'
    ]
    template_name = 'cinema_base/profile.html'
    extra_context = {
        'title': "Профиль пользователя",
        'default_image': settings.DEFAULT_USER_IMAGE,
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        q = UsersNotes.objects.filter(user_id=self.object.pk)
        context['notes'] = UsersNotes.objects.filter(user_id=self.object.pk)
        context['films'] = Film.objects.filter(pk__in=[x[0] for x in context['notes'].values_list('film_id')])
        return context

    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

class UserDelete(DeleteView):
    model = User
    template_name = 'cinema_base/user_delete.html'
    success_url = reverse_lazy('films_list')