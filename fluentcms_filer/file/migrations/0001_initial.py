# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('fluent_contents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerFileItem',
            fields=[
                ('contentitem_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='fluent_contents.ContentItem', on_delete=models.CASCADE)),
                ('name', models.CharField(max_length=255, null=True, verbose_name='name', blank=True)),
                ('target', models.CharField(default=b'', max_length=100, verbose_name='target', blank=True, choices=[(b'', 'same window'), (b'_blank', 'new window'), (b'_parent', 'parent window'), (b'_top', 'topmost frame')])),
                ('file', filer.fields.file.FilerFileField(verbose_name='file', to='filer.File', on_delete=models.CASCADE)),
            ],
            options={
                'db_table': 'contentitem_file_filerfileitem',
                'verbose_name': 'File',
                'verbose_name_plural': 'Files',
            },
            bases=('fluent_contents.contentitem',),
        ),
    ]
