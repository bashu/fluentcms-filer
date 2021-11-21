from django.test import TestCase
from django.core.files import File as DjangoFile
from django.core.files.uploadedfile import SimpleUploadedFile
from fluent_contents.tests.factories import create_content_item
from fluent_contents.tests.utils import render_content_items
from filer.models import Image

from fluentcms_filer.file.models import FilerFileItem as FileItem


class FileTests(TestCase):
    """
    Testing file plugin
    """

    def test_output(self):
        """
        Test the standard file
        """
        file_obj = SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpeg")

        image, _ = Image.objects.get_or_create(file=DjangoFile(file_obj), defaults={"name": "file.jpg"})

        item = create_content_item(FileItem, file=image, name="file.jpg")
        self.assertHTMLEqual(
            render_content_items([item]).html,
            '<p class="file">'
            f'<a href="{item.file.url}">'
            '<span class="filename">'
            'file.jpg<span class="filesize">'
            '(12 bytes)'
            '</span>'
            '</span>'
            '</a>'
            "</p>",
        )
