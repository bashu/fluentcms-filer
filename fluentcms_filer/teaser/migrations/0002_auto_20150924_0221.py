import fluent_contents.extensions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("teaser", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="filerteaseritem",
            name="description",
            field=fluent_contents.extensions.PluginHtmlField(null=True, verbose_name="description", blank=True),
        ),
    ]
