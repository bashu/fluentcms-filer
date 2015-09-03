# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from fluent_contents.extensions import ContentPlugin, plugin_pool

from .models import FilerFileItem


@plugin_pool.register
class FilerFilePlugin(ContentPlugin):
    model = FilerFileItem
    category = _('Filer')
    render_template = "fluentcms_filer/file.html"
