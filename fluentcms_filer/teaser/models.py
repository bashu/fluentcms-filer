# -*- coding: utf-8 -*-

from future.utils import python_2_unicode_compatible

from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.fields.image import FilerImageField

from fluent_contents.extensions import (
    PluginHtmlField, PluginUrlField)
from fluent_contents.models.db import ContentItem


@python_2_unicode_compatible
class FilerTeaserItem(ContentItem):

    title = models.CharField(_("title"), max_length=256)
    image = FilerImageField(verbose_name=_("image"), blank=True, null=True, on_delete=models.SET_NULL)
    url = PluginUrlField(_("URL"), null=True, blank=True,
        help_text=_("If present image will be clickable."))

    description = PluginHtmlField(_("description"), blank=True, null=True)

    target = models.CharField(_("target"), blank=True, max_length=100, choices=((
        ("", _("same window")),
        ("_blank", _("new window")),
        ("_parent", _("parent window")),
        ("_top", _("topmost frame")),
    )))

    class Meta:
        verbose_name = _("Teaser")
        verbose_name_plural = _("Teasers")

    def __str__(self):
        return self.title
