#coding: utf-8

from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    """Базовый класс с картинкой и описанием"""
    
    name = models.CharField(max_length=50, verbose_name=u"Название")
    #name_eng = models.CharField(max_length=50, verbose_name=u"Name")
    description = models.TextField(verbose_name=u"Описание", null=True)
    #description_eng = models.TextField(verbose_name=u"Description")
    
    class Meta:
        abstract = True


class TreeBaseModel(BaseModel):
    """дерево"""
    
    pid = models.ForeignKey("self", null=True, blank=True, verbose_name=u"сцыль на предка")
    #pic = models.ImageField(verbose_name=u"Картинка")

    class Meta:
        abstract = True


class Mine(TreeBaseModel):
    """Шахта"""
    
    class Meta:
        verbose_name = u'Шахта'
        verbose_name_plural = u'Шахты'
        db_table = 'mines'
     
        
class Plant(TreeBaseModel):
    """Плантация"""
    
    class Meta:
        verbose_name = u'Плантация'
        verbose_name_plural = u'Плантации'
        db_table = 'plants'
        
        
class EnergyPlant(TreeBaseModel):
    """Генератор энегрии"""
    
    class Meta:
        verbose_name = u'Генератор энегрии'
        verbose_name_plural = u'Генераторы энегрии'
        db_table = 'energy_generator'
        
        
class Race(TreeBaseModel):
    """Раса"""
    
    class Meta:
        verbose_name = u'Раса'
        verbose_name_plural = u'Расы'
        db_table = 'races'
        
        
class Citizen(TreeBaseModel):
    """Житель"""
    
    class Meta:
        verbose_name = u'Житель'
        verbose_name_plural = u'Жители'
        db_table = 'citizens'
        
        
class CelestialBody(TreeBaseModel):
    """Небесное тело"""
    
    class Meta:
        verbose_name = u'Небесное тело'
        verbose_name_plural = u'Небесные тела'
        db_table = 'celestial_bodies'
        
        
class ResourceType(BaseModel):
    """Тип ресурса"""
    
    class Meta:
        verbose_name = u'Тип ресурса'
        verbose_name_plural = u'Типы ресурсов'
        db_table = 'resource_types'
        
        
class ResourceSource(BaseModel):
    """Источник ресурса"""
    
    class Meta:
        verbose_name = u'Источник ресурса'
        verbose_name_plural = u'Источники ресурсов'
        db_table = 'resource_sources'
