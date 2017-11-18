# pyfolio

![build status](https://travis-ci.org/daniel-aguilar/pyfolio.svg?branch=master)

Folio is a Electronic Medical Record (EMR) tailored for a relative of mine.

pyfolio is the current implementation of Folio, which was previously written in PHP (Yii 2).

## Prerequisites

- Python 3
- PostgreSQL 9.6
- AWS S3 Access
- Make

## Building

Install the dependencies:  
`pip install -r requirements.txt`

Create a `.env` file in the root directory, with the following variables:

- `DATABASE_URL`: A valid PostgreSQL connection URI.

- `DJANGO_SETTINGS_MODULE`: The current Django settings you want to use. I recommend using the development settings: `'pyfolio.settings.dev'`.

- `AWS_ACCESS_KEY_ID` & `AWS_SECRET_ACCESS_KEY`: AWS access keys.

Run it:  
`./manage.py runserver`

## Testing

Run the `test` target:  
`make test`
