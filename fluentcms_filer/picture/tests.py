from django.test import TestCase
from django.core.files import File as DjangoFile
from django.core.files.uploadedfile import SimpleUploadedFile
from fluent_contents.tests.factories import create_content_item
from fluent_contents.tests.utils import render_content_items
from filer.models import Image

from fluentcms_filer.picture.models import FilerPictureItem as PictureItem


class PictureTests(TestCase):
    """
    Testing picture plugin
    """

    def test_output(self):
        """
        Test the standard picture
        """
        file_obj = SimpleUploadedFile("file.jpg", b"file_content", content_type="image/jpeg")

        image, _ = Image.objects.get_or_create(file=DjangoFile(file_obj), defaults={"name": "file.jpg"})

        item = create_content_item(PictureItem, image=image, caption="file.jpg")
        self.assertHTMLEqual(
            render_content_items([item]).html,
            '<figure class="picture ">'
            f'<img src="{item.image.url}" width="0.0" height="0.0" alt="" />'
            '<figcaption>file.jpg</figcaption>'
            '</figure>',
        )
