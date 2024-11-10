from datetime import date, datetime
from http.client import responses

from django.test import TestCase
from django.urls import reverse
from faker.generator import random

from cinema_base import factories, models
from cinema_base.factories import FilmFactory, StudioFactory
from cinema_base.models import Studio


class CinemaBaseTestCase(TestCase):
    def setUp(self):
        self.film = factories.FilmFactory()
        self.person = factories.ActorFactory()

    def test_get_actors_list(self):
        url = reverse('actors_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['actors'].count(), models.Person.objects.count())

    def test_get_detail_actor(self):
        url = reverse('actor_detail', kwargs={'pk':self.person.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_actor(self):
        url = reverse('actor_update', kwargs={'pk': self.person.pk})
        old_surname = self.person.surname
        old_birth_date = self.person.birth_date
        response = self.client.post(url, {
            'photo' : self.person.photo,
            'first_name' : 'новое имя',
            'surname' : 'новая фамилия',
            'birth_date' : date.today(),
            'gender': self.person.gender
        })
        self.person.refresh_from_db()
        self.assertNotEqual(old_surname, self.person.surname)
        self.assertNotEqual(old_birth_date, self.person.birth_date)
        self.assertEqual(response.status_code, 302)


    def test_create_actor(self):
        old_actors_count = models.Person.objects.count()
        url = reverse('actor_create')
        new_actor = factories.ActorFactory()
        response = self.client.put(url, {
            'photo': new_actor.photo,
            'first_name': new_actor.first_name,
            'surname': new_actor.surname,
            'birth_date': new_actor.birth_date,
            'gender': 'male'
        }, follow=True)
        self.assertLess(old_actors_count, models.Person.objects.count())

    def test_delete_actor(self):
        url = reverse('actor_delete', kwargs={'pk': self.person.pk})
        old_actor_count = models.Person.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_actor_count, models.Person.objects.count())

    def test_get_film_list(self):
        url = reverse('films_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['films'].count(), models.Film.objects.count())
    #
    def test_get_film_detail(self):
        url = reverse('film_detail', kwargs={'pk': self.film.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_film(self):
        url = reverse('film_delete', kwargs={'pk': self.film.pk})
        old_film_count = models.Film.objects.count()
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 302)
        self.assertGreater(old_film_count, models.Film.objects.count())

    # def test_update_film(self):
    #     url = reverse('film_update', kwargs={'pk': self.film.pk})
    #
    #     #url = 'films/1/update/'
    #
    #     old_title = self.film.title
    #     old_slogan = self.film.slogan
    #     print('\nСтарый')
    #     print(self.film.getinfo())
    #     # with open(ABSOLUTE_FILE_PATH) as file_object:
    #     #     data = {
    #     #         "title": "Demo Title",
    #     #         "author": "Demo Author",
    #     #         "subject": "Another Demo Subject",
    #     #         "details": "Another Demo Details",
    #     #         "file": file_object
    #     #     }
    #     #     response = self.client.post(self.book_create_url, data)
    #     #response = self.client.post(url, {
    #     print('дата')
    #
    #     print(self.film.getinfo())
    #     response = self.client.post(url, {
    #         'title': 'new_title',
    #         'poster': self.film.poster,
    #         'slogan': self.film.slogan,
    #         'release': self.film.release,
    #         'genres': self.film.genres,
    #         'studio': self.film.studio,
    #         'male_actor': self.film.male_actor,
    #         'female_actor': self.film.female_actor,
    #         'rating': self.film.rating,
    #         'duration': self.film.duration,
    #         'age': self.film.age,
    #     }, follow=True)
    #     #response = self.client.post(url, {'title': 'new_title'})
    #     #self.film.refresh_from_db(using=response.context['film'])
    #     self.film.refresh_from_db()
    #     #self.film = response.context['film']
    #
    #     print('Статус код')
    #     print(response.template_name)
    #     print(response.status_code)
    #     print(self.film.getinfo())
    #     #print()
    #     #self.assertEqual(response.status_code, 302)
    #     #self.assertNotEqual(self.film.title, old_title)
    #     # print('\nАпдейт')
    #     #print('Названия: ' + self.film.title + ' и ' + old_title + ' и ' + response.context['film'].title)
    #     #print(self.film.id)
    #     #print(response.context['film'].id)
    #     # print('Новый')
    #     # print(response.context['film'].getinfo())


    # def test_create_film(self):
    #     old_films_count = models.Film.objects.count()
    #     url = reverse('film_create')
    #     content = FilmFactory()
    #     response = self.client.put(url, content, folow=True)
    #     #response.redirect(reverse('films_list'))
    #     #response = self.client.get(reverse('films_list'))
    #     self.assertLess(old_films_count, models.Film.objects.count())
    #     print('response.request[]')
    #     print(response.request['PATH_INFO'])

    # def test_update_film(self):
    #
    #     #url = reverse('film_create')
    #     url = reverse('film_update', kwargs={'pk': self.film.pk})
    #     old = self.film.title
    #     print('cтарт')
    #     print(self.film.rating)
    #     print(self.film.studio)
    #     # print(models.Film.objects.filter(id=self.film.id).values_list('genres'))
    #     print(models.Film.objects.filter(id=self.film.id).values('genres'))
    #     print('cтарт')
    #     g = self.film.genres.values_list('id', flat=True)
    #     print('g')
    #     print(g)
    #     response = self.client.post(url, {
    #         'title' : 'тест тайтл222',
    #         #'poster' : 'тест постер222',
    #         'poster' : self.film.poster,
    #         #'release' : 'тест дата222',
    #         #'release' : date.today(),
    #         'release': date(2020,10,17),
    #         #'genres' : list(g),
    #         'genres' : [genre.id for genre in self.film.genres.all()],
    #         #'genres' : self.film.genres,
    #         #'genres' : 'тест жанры222',
    #         #'genres' : models.Film.objects.filter(id=self.film.id).values('genres'),
    #         #'studio' : 'тест студия222',
    #         'studio' : factories.StudioFactory(),
    #         'slogan' : 'тест слоган222',
    #         #'male_actor' : 'тест мужчина222',
    #         'male_actor' : self.film.male_actor.id,
    #         #'female_actor' : 'тест женщина222',
    #         'female_actor' : self.film.female_actor.id,
    #         #'rating' : 'тест рейтинг222',
    #         'rating' : random.randint(0, 100),
    #         #'duration' : 'тест дюрейшн222',
    #         'duration' : '1:2:30',
    #         #'age' : 'тест возраст222'
    #         'age' : 'R'
    #     }, follow=True)
    #     self.film.refresh_from_db()
    #     #models.Film.objects.filter(pk=self.film.pk).update(genres=[genre.id for genre in self.film.genres.all()])
    #     #self.film.refresh_from_db()
    #
    #     print('response.request[]')
    #     print(old)
    #     print(self.film.title)
    #     print(self.film.getinfo())
    #     print(self.film.poster)
    #     print(self.film.release)
    #     print(self.film.male_actor)
    #     print(self.film.male_actor.gender)
    #     print(self.film.female_actor)
    #     print(self.film.female_actor.gender)
    #     print(self.film.studio)
    #     print(self.film.rating)
    #     print(self.film.duration)
    #     print(self.film.age)
    #     print(response.status_code)
    #     print(response.context['film'].getinfo())
    #     self.film = response.context['film']
    #     print('И')
    #     print(self.film.getinfo())
    #     print(response.template_name)



        # url2 = reverse('films_list')
        # response2 = self.client.get(url2)
        # print('\nФильмс лист')
        # for _film in response2.context['films'].all():
        #     print(_film.getinfo())
        #     print(type(_film.duration))

        #print(self.film.objects.filter(id=self.film.id))

        # url = reverse('studio')
        # old = self.studio.name
        # response = self.client.post(url, {'name':'new_name'})
        # self.studio.refresh_from_db()
        # print('response.request[]')
        # print(old)
        # print(self.studio.name)
        # print(response.status_code)
