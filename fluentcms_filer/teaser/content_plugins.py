from django.utils.translation import gettext_lazy as _
from fluent_contents.extensions import ContentPlugin, plugin_pool

from .models import FilerTeaserItem


@plugin_pool.register
class FilerTeaserPlugin(ContentPlugin):
    model = FilerTeaserItem
    category = _("Filer")
    admin_form_template = "admin/fluentcms_filer/teaser/admin_form.html"
    admin_init_template = "admin/fluentcms_filer/teaser/admin_init.html"
    render_template = "fluentcms_filer/teaser.html"

    fieldsets = (
        (
            None,
            {
                "fields": ("title", "image", "description"),
            },
        ),
        (
            _("read more link"),
            {
                "fields": ("url", "url_title", "target"),
            },
        ),
    )

    class Media:
        css = {"screen": ("fluentcms_filer/teaser/admin.css",)}
