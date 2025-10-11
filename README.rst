=========
 pyfolio
=========

.. image:: https://github.com/daniel-aguilar/pyfolio/workflows/build/badge.svg
    :target: https://github.com/daniel-aguilar/pyfolio/actions

.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Ruff

Folio is an Electronic Medical Record (EMR) tailored for a relative of mine.

pyfolio is the current implementation of Folio, which was previously written in
PHP (Yii 2).

Requirements
============

* Python 3.13
* Make
* PostgreSQL 15
* `AWS S3`_

Building
========

Install the dependencies::

    pip install -r requirements.txt

Create a ``.env`` file in the root directory, with the following variables:

* ``DATABASE_URL``: A `PostgreSQL connection URI`_.
* ``DJANGO_SETTINGS_MODULE``: The current Django settings you want to use (e.g.
  ``pyfolio.settings.dev``).
* ``AWS_ACCESS_KEY_ID`` & ``AWS_SECRET_ACCESS_KEY``: AWS access keys.

Run it::

    ./manage.py runserver

Testing
=======

Run the ``test`` target::

    make test

.. _`AWS S3`: https://aws.amazon.com/s3/
.. _`PostgreSQL connection URI`: https://www.postgresql.org/docs/15/libpq-connect.html#LIBPQ-CONNSTRING
