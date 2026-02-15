=========
 pyfolio
=========

.. image:: https://github.com/daniel-aguilar/pyfolio/workflows/build/badge.svg
    :target: https://github.com/daniel-aguilar/pyfolio/actions

Folio is an Electronic Medical Record (EMR) tailored for a relative of
mine.

pyfolio is the current implementation of Folio, which was previously
written in PHP (Yii 2).

Requirements
============

* Python & `uv`_ (see ``pyproject.toml`` for required versions)
* Make
* PostgreSQL 15
* `AWS S3`_

Building
========

Install the dependencies::

    make install-dev

Create a ``.env`` file in the root directory with the required
variables:

* ``DATABASE_URL``: A `PostgreSQL connection URI`_.
* ``DJANGO_SETTINGS_MODULE``: The current Django settings to use (e.g.
  ``pyfolio.settings.development`` for development,
  ``pyfolio.settings.production`` for production).
* ``AWS_ACCESS_KEY_ID`` & ``AWS_SECRET_ACCESS_KEY``: AWS access keys
  (for production with S3).

Run the development server::

    ./manage.py runserver

Testing
=======

Run the ``test`` target::

    make test

.. _`uv`: https://github.com/astral-sh/uv
.. _`AWS S3`: https://aws.amazon.com/s3/
.. _`PostgreSQL connection URI`: https://www.postgresql.org/docs/15/libpq-connect.html#LIBPQ-CONNSTRING
