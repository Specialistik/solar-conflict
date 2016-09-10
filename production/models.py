#coding: utf-8

from django.db import models
from core.models import BaseModel, ResourceType


class BaseFactory(BaseModel):
    """Базовый класс всех фабрик"""

    resources = models.ManyToManyField(to=ResourceType, verbose_name=u"Необходимые ресурсы")
    hp = models.IntegerField(verbose_name=u"Хит поинты здания")
    factory_armor = models.IntegerField(verbose_name=u"Броня сдания")


class RocketEngineFactory(BaseFactory):
    """Фабрика ракетных двигателей"""
    
    class Meta:
        verbose_name = u'Фабрика ракетных двигателей'
        verbose_name_plural = u'Фабрики ракетных двигателей'
        db_table = 'rocket_engine_factories'
        
        
class WeaponFactory(BaseFactory):
    """Фабрика оружия"""
    
    class Meta:
        verbose_name = u'Фабрика оружия'
        verbose_name_plural = u'Фабрики оружия'
        db_table = 'weapon_factories'


class ArmorFactory(BaseFactory):
    """Фабрика брони"""

    class Meta:
        verbose_name = u'Фабрика брони'
        verbose_name_plural = u'Фабрики брони'
        db_table = 'armor_factories'


class SpaceShipFactory(BaseFactory):
    """Фабрика космических кораблей"""

    class Meta:
        verbose_name = u'Фабрика космических кораблей'
        verbose_name_plural = u'Фабрики космических кораблей'
        db_table = 'space_ship_factories'
