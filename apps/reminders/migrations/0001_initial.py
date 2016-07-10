# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlertMethod',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('type', models.IntegerField(unique=True, default=0, choices=[(0, 'Email'), (1, 'Message')])),
                ('name', models.CharField(max_length=32)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 17, 211602))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 17, 211626))),
            ],
        ),
        migrations.CreateModel(
            name='Reminder',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('alert_at', models.DateTimeField()),
                ('message', models.CharField(null=True, blank=True, max_length=254)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 17, 212858))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 17, 212878))),
                ('method', models.ManyToManyField(to='reminders.AlertMethod')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 17, 210190))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 17, 210215))),
            ],
        ),
        migrations.CreateModel(
            name='TemplateVariable',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 17, 209525))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 17, 209564))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(null=True, blank=True, max_length=4)),
                ('first_name', models.CharField(null=True, blank=True, max_length=32)),
                ('last_name', models.CharField(null=True, blank=True, max_length=32)),
                ('email', models.CharField(unique=True, max_length=64)),
                ('mobile_no', models.IntegerField(null=True, blank=True, unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 17, 212217))),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 17, 212241))),
            ],
        ),
        migrations.AddField(
            model_name='template',
            name='variables',
            field=models.ManyToManyField(to='reminders.TemplateVariable'),
        ),
        migrations.AddField(
            model_name='reminder',
            name='template',
            field=models.ForeignKey(to='reminders.Template', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='reminder',
            name='user',
            field=models.ForeignKey(to='reminders.User'),
        ),
    ]
