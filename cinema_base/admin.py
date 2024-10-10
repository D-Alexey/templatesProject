from django.contrib import admin
from cinema_base import models

#Register your models here.
@admin.register(models.Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(models.Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(models.Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', )

@admin.register(models.Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', )

# @admin.register(models.Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', )
#
# @admin.register(models.Author)
# class AuthorAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'surname', )
#
# @admin.register(models.Genre)
# class GenreAdmin(admin.ModelAdmin):
#     list_display = ('name', )
#
# @admin.register(models.Storage)
# class StorageAdmin(admin.ModelAdmin):
#     list_display = ('amount', )