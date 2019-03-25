# -*- coding: utf-8 -*-

from future.builtins import str
from future.utils import python_2_unicode_compatible

from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.fields.image import FilerImageField

from fluent_contents.extensions import PluginUrlField
from fluent_contents.models.db import ContentItem


@python_2_unicode_compatible
class FilerPictureItem(ContentItem):
    ALIGN_LEFT = 'left'
    ALIGN_CENTER = 'center'
    ALIGN_RIGHT = 'right'
    ALIGN_CHOICES = (
        (ALIGN_LEFT, _("Left")),
        (ALIGN_CENTER, _("Center")),
        (ALIGN_RIGHT, _("Right")),
    )

    image = FilerImageField(verbose_name=_("image"), on_delete=models.CASCADE)
    caption = models.TextField(_("caption"), blank=True)
    align = models.CharField(_("align"), max_length=10, choices=ALIGN_CHOICES, blank=True)

    url = PluginUrlField(_("URL"), blank=True)
    in_new_window = models.BooleanField(_("open in a new window"), default=False, blank=True)

    class Meta:
        verbose_name = _("Picture")
        verbose_name_plural = _("Pictures")

    def __str__(self):
        return self.caption or str(self.image)

    @property
    def align_class(self):
        if self.align == self.ALIGN_LEFT:
            return 'align-left'
        elif self.align == self.ALIGN_CENTER:
            return 'align-center'
        elif self.align == self.ALIGN_RIGHT:
            return 'align-right'
        else:
            return ''
