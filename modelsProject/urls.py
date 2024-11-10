"""
URL configuration for modelsProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from cinema_base import views

router = DefaultRouter()

router.register('persons_api', views.PersonAPI, basename='persons')
router.register('films_api', views.FilmAPI, basename='films')
router.register('genres_api', views.GenreAPI, basename='genres')
router.register('studios_api', views.StudioAPI, basename='studio')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('first_view/', views.FirstView.as_view(), name='first_view'),
    path('films/', views.FilmsList.as_view(), name='films_list'),
    path('films/<int:pk>/', views.FilmDetail.as_view(), name='film_detail'),
    path('film_create/', views.FilmCreate.as_view(), name='film_create'),
    path('films/<int:pk>/update/', views.FilmsUpdate.as_view(), name='film_update'),
    path('films/<int:pk>/delete/', views.FilmsDelete.as_view(), name='film_delete'),
    path('actors/', views.ActorsList.as_view(), name='actors_list'),
    path('directors/', views.DirectorsList.as_view(), name='directors_list'),
    path('person/<int:pk>/', views.PersonDetail.as_view(), name='person_detail'),
    path('person_create/', views.PersonCreate.as_view(), name='person_create'),
    path('persons/<int:pk>/update/', views.PersonUpdate.as_view(), name='person_update'),
    path('persons/<int:pk>/delete/', views.PersonDelete.as_view(), name='person_delete'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.ProfileUser.as_view(), name='profile'),
    path('user_delete/<int:pk>/', views.UserDelete.as_view(), name='user_delete'),
    path('note_create/<int:pk>', views.NoteCreate.as_view(), name='note_create'),
    path('note_delete/<int:pk>', views.NoteDelete.as_view(), name='note_delete'),
    path('note_update/<int:pk>', views.NoteUpdate.as_view(), name='note_update'),
] + router.urls
