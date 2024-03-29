#!/usr/bin/env python
import sys

import django
from django.conf import settings
from django.core.management import execute_from_command_line

if not settings.configured:
    settings.configure(
        SECRET_KEY="YOUR_SECRET_KEY",
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": ":memory:",
            },
        },
        SITE_ID=1,
        INSTALLED_APPS=(
            "django.contrib.contenttypes",
            "django.contrib.admin",
            "django.contrib.auth",
            "django.contrib.messages",
            "django.contrib.sites",
            "fluent_contents",
            "fluent_contents.tests.testapp",
            "filer",
            "easy_thumbnails",
            "fluentcms_filer.file",
            "fluentcms_filer.picture",
            "fluentcms_filer.teaser",
        ),
        MIDDLEWARE=(
            "django.contrib.auth.middleware.AuthenticationMiddleware",
            "django.contrib.messages.middleware.MessageMiddleware",
            "django.contrib.sessions.middleware.SessionMiddleware"
        ),
        TEMPLATES=[
            {
                "BACKEND": "django.template.backends.django.DjangoTemplates",
                "DIRS": (),
                "OPTIONS": {
                    "loaders": (
                        "django.template.loaders.filesystem.Loader",
                        "django.template.loaders.app_directories.Loader",
                    ),
                    "context_processors": (
                        "django.template.context_processors.debug",
                        "django.template.context_processors.i18n",
                        "django.template.context_processors.media",
                        "django.template.context_processors.request",
                        "django.template.context_processors.static",
                        "django.contrib.messages.context_processors.messages",
                        "django.contrib.auth.context_processors.auth",
                    ),
                },
            },
        ],
        FLUENT_CONTENTS_CACHE_OUTPUT=False,
        TEST_RUNNER="django.test.runner.DiscoverRunner",
        DEFAULT_AUTO_FIELD="django.db.models.BigAutoField",
    )

DEFAULT_TEST_APPS = [
    "fluentcms_filer.file",
    "fluentcms_filer.picture",
    "fluentcms_filer.teaser"
]


def runtests():
    other_args = list(filter(lambda arg: arg.startswith("-"), sys.argv[1:]))
    test_apps = (
        list(filter(lambda arg: not arg.startswith("-"), sys.argv[1:])) or DEFAULT_TEST_APPS
    )
    argv = sys.argv[:1] + ["test", "--traceback"] + other_args + test_apps
    execute_from_command_line(argv)


if __name__ == "__main__":
    runtests()
