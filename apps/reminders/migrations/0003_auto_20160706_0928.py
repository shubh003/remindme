# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('reminders', '0002_auto_20160705_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alertmethod',
            name='name',
        ),
        migrations.AlterField(
            model_name='alertmethod',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 9, 28, 19, 316257)),
        ),
        migrations.AlterField(
            model_name='alertmethod',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 9, 28, 19, 316279)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 9, 28, 19, 317439)),
        ),
        migrations.AlterField(
            model_name='reminder',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 9, 28, 19, 317458)),
        ),
        migrations.AlterField(
            model_name='template',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 9, 28, 19, 315090)),
        ),
        migrations.AlterField(
            model_name='template',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 9, 28, 19, 315114)),
        ),
        migrations.AlterField(
            model_name='templatevariable',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 9, 28, 19, 314520)),
        ),
        migrations.AlterField(
            model_name='templatevariable',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 9, 28, 19, 314551)),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 9, 28, 19, 316833)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 6, 9, 28, 19, 316853)),
        ),
    ]
