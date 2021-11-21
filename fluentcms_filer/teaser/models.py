from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField
from fluent_contents.extensions import PluginHtmlField, PluginUrlField
from fluent_contents.models.db import ContentItem


class FilerTeaserItem(ContentItem):

    title = models.CharField(_("title"), max_length=256)
    image = FilerImageField(verbose_name=_("image"), blank=True, null=True, on_delete=models.SET_NULL)
    url = PluginUrlField(_("URL"), null=True, blank=True, help_text=_("If present image will be clickable."))
    url_title = models.CharField(_("URL title"), max_length=200, blank=True, null=True)

    description = PluginHtmlField(_("description"), blank=True, null=True)

    target = models.CharField(
        _("target"),
        blank=True,
        max_length=100,
        choices=(
            (
                ("", _("same window")),
                ("_blank", _("new window")),
                ("_parent", _("parent window")),
                ("_top", _("topmost frame")),
            )
        ),
    )

    class Meta:
        verbose_name = _("Teaser")
        verbose_name_plural = _("Teasers")

    def __str__(self):
        return self.title
