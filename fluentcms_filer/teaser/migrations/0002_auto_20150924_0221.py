# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import fluent_contents.extensions


class Migration(migrations.Migration):

    dependencies = [
        ('teaser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filerteaseritem',
            name='description',
            field=fluent_contents.extensions.PluginHtmlField(null=True, verbose_name='description', blank=True),
        ),
    ]
