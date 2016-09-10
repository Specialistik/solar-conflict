#coding: utf-8

from django.contrib import admin
from production.models import RocketEngineFactory, ArmorFactory, WeaponFactory, SpaceShipFactory

admin.site.register(RocketEngineFactory)
admin.site.register(ArmorFactory)
admin.site.register(WeaponFactory)
admin.site.register(SpaceShipFactory)
