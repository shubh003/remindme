# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alertmethod',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 50, 750622)),
        ),
        migrations.AlterField(
            model_name='alertmethod',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 50, 750647)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 50, 751937)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 50, 751961)),
        ),
        migrations.AlterField(
            model_name='template',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 50, 749343)),
        ),
        migrations.AlterField(
            model_name='template',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 50, 749368)),
        ),
        migrations.AlterField(
            model_name='templatevariable',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 50, 748736)),
        ),
        migrations.AlterField(
            model_name='templatevariable',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 50, 748775)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 50, 751249)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 5, 23, 36, 50, 751276)),
        ),
    ]
