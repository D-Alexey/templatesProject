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

from cinema_base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_view/', views.FirstView.as_view(), name='first_view'),
    # path('films/', views.FilmsListTemplateView.as_view(), name='list_view'),
    # path('films_list/', views.FilmsList.as_view(), name='films_list'),
    path('films/', views.FilmsList.as_view(), name='films_list'),
    path('gosling/', views.GoslingFilms.as_view(), name='gosling_films'),
    path('films/<int:pk>/', views.FilmDetail.as_view(), name='film_detail'),
    path('film_create/', views.FilmCreate.as_view(), name='film_create'),
    path('films/<int:pk>/update/', views.FilmsUpdate.as_view(), name='film_update'),
    path('films/<int:pk>/delete/', views.FilmsDelete.as_view(), name='film_delete'),
    path('actors/', views.ActorsList.as_view(), name='actors_list'),
    path('actor/<int:pk>/', views.ActorDetail.as_view(), name='actor_detail'),
    path('actor_create/', views.ActorCreate.as_view(), name='actor_create'),
    path('actors/<int:pk>/update/', views.ActorUpdate.as_view(), name='actor_update'),
    path('actors/<int:pk>/delete/', views.ActorDelete.as_view(), name='actor_delete'),
]
