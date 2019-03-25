# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import fluent_contents.extensions


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('fluent_contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerTeaserItem',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fluent_contents.ContentItem', on_delete=models.CASCADE)),
                ('title', models.CharField(max_length=256, verbose_name='title')),
                ('url', fluent_contents.extensions.PluginUrlField(help_text='If present image will be clickable.', max_length=300, null=True, verbose_name='URL', blank=True)),
                ('description', models.TextField(null=True, verbose_name='description', blank=True)),
                ('target', models.CharField(blank=True, max_length=100, verbose_name='target', choices=[(b'', 'same window'), (b'_blank', 'new window'), (b'_parent', 'parent window'), (b'_top', 'topmost frame')])),
                ('image', filer.fields.image.FilerImageField(verbose_name='image', blank=True, to='filer.Image', null=True, on_delete=models.SET_NULL)),
            ],
            options={
                'db_table': 'contentitem_teaser_filerteaseritem',
                'verbose_name': 'Teaser',
                'verbose_name_plural': 'Teasers',
            },
            bases=('fluent_contents.contentitem',),
        ),
    ]
