# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-08-25 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('production', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('armor_power', models.PositiveIntegerField(verbose_name='Сила брони')),
            ],
            options={
                'db_table': 'armors',
                'verbose_name': 'Броня',
                'verbose_name_plural': 'Броня',
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='ArmorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'db_table': 'armor_types',
                'verbose_name': 'Тип брони',
                'verbose_name_plural': 'Типы брони',
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='RocketEngine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('rocket_engine_power', models.PositiveIntegerField(verbose_name='Сила ракетного двигателя')),
                ('rocket_engine_factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.SpaceShipFactory', verbose_name='Фабрика ракетных двигателей')),
            ],
            options={
                'db_table': 'rocket_engines',
                'verbose_name': 'Ракетный двигатель',
                'verbose_name_plural': 'Ракетные двигатели',
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='RocketEngineType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'db_table': 'rocket_engine_types',
                'verbose_name': 'Тип ракетного двигателя',
                'verbose_name_plural': 'Типы ракетных двигателей',
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='SpaceShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('rocket_engines', models.ManyToManyField(to='military.RocketEngine', verbose_name='Ракетные двигатели')),
                ('space_ship_factory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.SpaceShipFactory', verbose_name='Фабрика космических кораблей')),
            ],
            options={
                'db_table': 'space_ships',
                'verbose_name': 'Тип ракетного двигателя',
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='SpaceShipType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'db_table': 'space_ship_types',
                'verbose_name': 'Тип космического корабля',
                'verbose_name_plural': 'Типы космических кораблей',
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('damage_min', models.PositiveIntegerField(verbose_name='Минимальный урон')),
                ('damage_max', models.PositiveIntegerField(verbose_name='Максимальный урон')),
            ],
            options={
                'db_table': 'weapons',
                'verbose_name': 'Орудие',
                'verbose_name_plural': 'Орудия',
                'indexes': [],
            },
        ),
        migrations.CreateModel(
            name='WeaponType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
            ],
            options={
                'db_table': 'weapon_types',
                'verbose_name': 'Тип орудия',
                'verbose_name_plural': 'Типы орудий',
                'indexes': [],
            },
        ),
        migrations.AddField(
            model_name='weapon',
            name='damage_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='military.WeaponType', verbose_name='Тип урона'),
        ),
        migrations.AddField(
            model_name='weapon',
            name='weapon_factory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.WeaponFactory', verbose_name='Фабрика орудий'),
        ),
        migrations.AddField(
            model_name='spaceship',
            name='space_ship_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='military.SpaceShipType', verbose_name='Тип космического корабля'),
        ),
        migrations.AddField(
            model_name='spaceship',
            name='weapons',
            field=models.ManyToManyField(to='military.Weapon', verbose_name='Корабельные орудия'),
        ),
        migrations.AddField(
            model_name='rocketengine',
            name='rocket_engine_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='military.RocketEngineType', verbose_name='Тип ракетного двигателя'),
        ),
        migrations.AddField(
            model_name='armor',
            name='armor_factory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='military.ArmorType', verbose_name='Фабрика брони'),
        ),
        migrations.AddField(
            model_name='armor',
            name='armor_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='production.ArmorFactory', verbose_name='Тип брони'),
        ),
    ]
