# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-04-18 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_remove_users_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password',
            field=models.CharField(default='null', max_length=255),
            preserve_default=False,
        ),
    ]
