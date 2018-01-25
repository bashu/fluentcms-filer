# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _

from fluent_contents.extensions import ContentPlugin, plugin_pool

from .models import FilerFileItem


@plugin_pool.register
class FilerFilePlugin(ContentPlugin):
    model = FilerFileItem
    category = _('Filer')
    admin_form_template = "admin/fluentcms_filer/file/admin_form.html"
    admin_init_template = "admin/fluentcms_filer/file/admin_init.html"
    render_template = "fluentcms_filer/file.html"

    class Media:
        css = {
            'screen': (
                'fluentcms_filer/file/admin.css',
            )
        }    
