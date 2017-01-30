import re

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
]

if settings.SERVE_MEDIA:
    from django.views.static import serve

    urlpatterns += [
        url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve, kwargs={
            'document_root': settings.STATIC_ROOT,
        }),
    ]

    urlpatterns += [
        url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), serve, kwargs={
            'document_root': settings.MEDIA_ROOT,
        }),
    ]

urlpatterns += [
    url(r'', include('fluent_pages.urls')),
]
