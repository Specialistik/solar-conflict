#coding: utf-8

from django.contrib import admin
from core.models import Race, Citizen, CelestialBody, ResourceType, ResourceSource


class RaceAdmin(admin.ModelAdmin):
    fields = ('description', 'name')
    list_display = ('description', 'name')


class CitizenAdmin(admin.ModelAdmin):
    list_display = ('description', )


class CelestialBodyAdmin(admin.ModelAdmin):
    fields = ('description', 'name', 'pid')
    list_display = ('description', 'name', 'pid')


class ResourceTypeAdmin(admin.ModelAdmin):
    fields = ('description', 'name')
    list_display = ('description', 'name')


class ResourceSourceAdmin(admin.ModelAdmin):
    fields = ('description', 'name')
    list_display = ('description', 'name')

admin.site.register(Race, RaceAdmin)
admin.site.register(Citizen, CitizenAdmin)
admin.site.register(CelestialBody, CelestialBodyAdmin)
admin.site.register(ResourceType, ResourceTypeAdmin)
admin.site.register(ResourceSource, ResourceSourceAdmin)
