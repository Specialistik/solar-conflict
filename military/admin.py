#coding: utf-8

from django.contrib import admin
from military.models import *

admin.site.register(WeaponType)
admin.site.register(Weapon)
admin.site.register(ArmorType)
admin.site.register(Armor)
admin.site.register(RocketEngineType)
admin.site.register(RocketEngine)
admin.site.register(SpaceShipType)
admin.site.register(SpaceShip)

