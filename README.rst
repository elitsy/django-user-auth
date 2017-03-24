django-user-auth
================

Overview
~~~~~~~~

Videos application for django social network framework Edit


Installation
~~~~~~~~~~~~

Install work version using PIP::

    pip install -e git+ssh://git@github.com/elitsy/django-user-auth.git@0.0.1#egg=user_auth

Change ``settings.py`` of your project. Add ``user_auth`` to
``INSTALLED_APPS``. Add required options (see: Settings).

Run ``manage.py migrate`` and restart your project server.


Settings
~~~~~~~~

No any settings required


Usage
~~~~~

Install it, plug-in to your project and add required settings. Have fun!


Provided template tags and libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No any templeate tags provided


Provided management commands
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No any management commands provided


Testing
~~~~~~~

If this application is installed in your project you can run this inside your
project::

    python manage.py test user_auth

or instead run inside this package::

    python run_tests.py

or with tox::

    tox
