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
            name='FilerPictureItem',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fluent_contents.ContentItem', on_delete=models.CASCADE)),
                ('caption', models.TextField(verbose_name='caption', blank=True)),
                ('align', models.CharField(blank=True, max_length=10, verbose_name='align', choices=[(b'left', 'Left'), (b'center', 'Center'), (b'right', 'Right')])),
                ('url', fluent_contents.extensions.PluginUrlField(max_length=300, verbose_name='URL', blank=True)),
                ('in_new_window', models.BooleanField(default=False, verbose_name='open in a new window')),
                ('image', filer.fields.image.FilerImageField(verbose_name='image', to='filer.Image', on_delete=models.CASCADE)),
            ],
            options={
                'db_table': 'contentitem_picture_filerpictureitem',
                'verbose_name': 'Picture',
                'verbose_name_plural': 'Pictures',
            },
            bases=('fluent_contents.contentitem',),
        ),
    ]
