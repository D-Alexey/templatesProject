from django.contrib import admin
from cinema_base import models
from django.contrib.auth.admin import UserAdmin

#Register your models here.
admin.site.register(models.User, UserAdmin)

@admin.register(models.Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(models.Studio)
class StudioAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(models.Person)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', )

@admin.register(models.Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name',)
