fluentcms-filer
===============

django-filer_ content plugins for django-fluent-contents_

.. image:: https://img.shields.io/pypi/v/fluentcms-filer.svg
    :target: https://pypi.python.org/pypi/fluentcms-filer/

.. image:: https://img.shields.io/pypi/dm/fluentcms-filer.svg
    :target: https://pypi.python.org/pypi/fluentcms-filer/

.. image:: https://img.shields.io/github/license/bashu/fluentcms-filer.svg
    :target: https://pypi.python.org/pypi/fluentcms-filer/

Installation
============

First install the module, preferably in a virtual environment. It can be installed from PyPI:

.. code-block:: shell

    pip install fluentcms-filer


Backend Configuration
---------------------

First make sure the project is configured for both django-fluent-contents_ and django-filer_.

Then add the following settings:

.. code-block:: python

    INSTALLED_APPS += (
        'fluentcms_filer.file',
        'fluentcms_filer.picture',
        'fluentcms_filer.teaser',
    )

The database tables can be created afterwards:

.. code-block:: shell

    python ./manage.py migrate

Now, the ``FilerFilePlugin``, ``FilerPicturePlugin`` and ``FilerTeaserPlugin`` can be added to your ``PlaceholderField`` and ``PlaceholderEditorAdmin`` admin screens.

Frontend Configuration
----------------------

If needed, the HTML code can be overwritten by redefining ``fluentcms_filer/[file|picture|teaser].html``.

Contributing
------------

If you like this module, forked it, or would like to improve it, please let us know!
Pull requests are welcome too. :-)

.. _django-fluent-contents: https://github.com/edoburu/django-fluent-contents
.. _django-filer: http://django-filer.readthedocs.org/en/latest/installation.html#configuration
