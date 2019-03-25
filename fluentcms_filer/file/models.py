# -*- coding: utf-8 -*-

from future.builtins import str
from future.utils import python_2_unicode_compatible

from django.db import models
from django.utils.translation import ugettext_lazy as _

from filer.fields.file import FilerFileField

from fluent_contents.models.db import ContentItem


@python_2_unicode_compatible
class FilerFileItem(ContentItem):

    file = FilerFileField(verbose_name=_("file"), on_delete=models.CASCADE)
    name = models.CharField(_("name"), max_length=255, null=True, blank=True)

    target = models.CharField(_("target"), blank=True, max_length=100, choices=((
        ("", _("same window")),
        ("_blank", _("new window")),
        ("_parent", _("parent window")),
        ("_top", _("topmost frame")),
    )), default='')

    class Meta:
        verbose_name = _("File")
        verbose_name_plural = _("Files")

    @property
    def filename(self):
        if self.file.name in ('', None):
            return self.file.original_filename
        return self.file.name
    
    def __str__(self):
        if self.name:
            return self.name
        elif self.file:
            return str(self.filename)
        return "<empty>"
