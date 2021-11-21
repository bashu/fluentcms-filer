from django.test import TestCase
from fluent_contents.tests.factories import create_content_item
from fluent_contents.tests.utils import render_content_items

from fluentcms_filer.teaser.models import FilerTeaserItem as TeaserItem


class TeaserTests(TestCase):
    """
    Testing teaser plugin
    """

    def test_output(self):
        """
        Test the standard teaser
        """
        item = create_content_item(TeaserItem, url="http://example.com", title="TEST")
        self.assertHTMLEqual(
            render_content_items([item]).html,
            '<div class="teaser">'
            "  <h2>TEST</h2>"
            '  <a href="http://example.com" class="readmore">more &#187;</a>'
            "</div>",
        )
