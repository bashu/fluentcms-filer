# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from fluent_contents.extensions import ContentPlugin, plugin_pool

from .models import FilerTeaserItem


@plugin_pool.register
class FilerTeaserPlugin(ContentPlugin):
    model = FilerTeaserItem
    category = _('Filer')
    render_template = "fluentcms_filer/teaser.html"
