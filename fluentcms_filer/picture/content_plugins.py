# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from django.contrib.admin.widgets import AdminTextareaWidget

from fluent_contents.extensions import ContentPlugin, plugin_pool

from .models import FilerPictureItem


@plugin_pool.register
class FilerPicturePlugin(ContentPlugin):
    model = FilerPictureItem
    category = _('Filer')
    admin_form_template = "admin/fluentcms_filer/picture/admin_form.html"
    admin_init_template = "admin/fluentcms_filer/picture/admin_init.html"
    render_template = "fluentcms_filer/picture.html"

    formfield_overrides = {
        'caption': {
            'widget': AdminTextareaWidget(attrs={'cols': 30, 'rows': 4, 'class': 'vTextField'}),
        },
    }
    radio_fields = {
        'align': ContentPlugin.HORIZONTAL
    }

    class Media:
        css = {
            'screen': (
                'fluentcms_filer/picture/admin.css',
            )
        }    
