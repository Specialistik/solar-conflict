#coding: utf-8

from django.db import models
from core.models import BaseModel
from production.models import ArmorFactory, RocketEngineFactory, SpaceShipFactory, WeaponFactory


class WeaponType(BaseModel):
    """Тип орудий"""

    class Meta:
        verbose_name = u'Тип орудия'
        verbose_name_plural = u'Типы орудий'
        db_table = 'weapon_types'


class Weapon(BaseModel):
    """Орудия"""

    weapon_factory = models.ForeignKey(WeaponFactory, verbose_name=u"Фабрика орудий")
    damage_type = models.ForeignKey(WeaponType, verbose_name=u"Тип урона")
    damage_min = models.PositiveIntegerField(verbose_name=u"Минимальный урон")
    damage_max = models.PositiveIntegerField(verbose_name=u"Максимальный урон")

    class Meta:
        verbose_name = u'Орудие'
        verbose_name_plural = u'Орудия'
        db_table = 'weapons'


class ArmorType(BaseModel):
    """Тип брони"""

    class Meta:
        verbose_name = u'Тип брони'
        verbose_name_plural = u'Типы брони'
        db_table = 'armor_types'


class Armor(BaseModel):
    """Броня"""

    armor_factory = models.ForeignKey(ArmorType, verbose_name=u"Фабрика брони")
    armor_type = models.ForeignKey(ArmorFactory, verbose_name=u"Тип брони")
    armor_power = models.PositiveIntegerField(verbose_name=u"Сила брони")

    class Meta:
        verbose_name = u'Броня'
        verbose_name_plural = u'Броня'
        db_table = 'armors'


class RocketEngineType(BaseModel):
    """Тип брони"""

    class Meta:
        verbose_name = u'Тип ракетного двигателя'
        verbose_name_plural = u'Типы ракетных двигателей'
        db_table = 'rocket_engine_types'


class RocketEngine(BaseModel):
    """Тип ракетного двигателя"""

    rocket_engine_factory = models.ForeignKey(SpaceShipFactory, verbose_name=u"Фабрика ракетных двигателей")
    rocket_engine_type = models.ForeignKey(RocketEngineType, verbose_name=u"Тип ракетного двигателя")
    rocket_engine_power = models.PositiveIntegerField(verbose_name=u"Сила ракетного двигателя")

    class Meta:
        verbose_name = u'Ракетный двигатель'
        verbose_name_plural = u'Ракетные двигатели'
        db_table = 'rocket_engines'


class SpaceShipType(BaseModel):
    """Тип космического корабля"""

    class Meta:
        verbose_name = u'Тип космического корабля'
        verbose_name_plural = u'Типы космических кораблей'
        db_table = 'space_ship_types'


class SpaceShip(BaseModel):
    """Ракетные двигатели"""

    space_ship_factory = models.ForeignKey(SpaceShipFactory, verbose_name=u"Фабрика космических кораблей")
    space_ship_type = models.ForeignKey(SpaceShipType, verbose_name=u"Тип космического корабля")
    weapons = models.ManyToManyField(Weapon, verbose_name=u"Корабельные орудия")
    rocket_engines = models.ManyToManyField(RocketEngine, verbose_name=u"Ракетные двигатели")

    class Meta:
        verbose_name = u'Тип ракетного двигателя'
        db_table = 'space_ships'
