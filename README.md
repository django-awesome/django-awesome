# Django Awesome

The curated list of awesome libraries incorporated into a project, ready to form the core for projects of any scale and can be deployed to production right after pulling the code.

[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/django-awesome/django-awesome/badges/quality-score.png?b=main)](https://scrutinizer-ci.com/g/django-awesome/django-awesome/?branch=main)
[![Code Coverage](https://scrutinizer-ci.com/g/django-awesome/django-awesome/badges/coverage.png?b=main)](https://scrutinizer-ci.com/g/django-awesome/django-awesome/?branch=main)
[![Build Status](https://scrutinizer-ci.com/g/django-awesome/django-awesome/badges/build.png?b=main)](https://scrutinizer-ci.com/g/django-awesome/django-awesome/build-status/main)
[![Code Intelligence Status](https://scrutinizer-ci.com/g/django-awesome/django-awesome/badges/code-intelligence.svg?b=main)](https://scrutinizer-ci.com/code-intelligence)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/django-awesome/django-awesome/main.svg)](https://results.pre-commit.ci/latest/github/django-awesome/django-awesome/main)

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

License: MIT

## Release Features

_For a complete listing of all improvements, see [Django Awesome](https://django-awesome.github.io/)_

#### Admin

- [x] [django-grappelli](https://github.com/sehmaschine/django-grappelli) - A jazzy skin for the admin.
- [x] Apply [Oswald](https://keenthemes.com/products/oswald-html-free) override Grappelli template
- [x] Custom admin menu inherited from [django-admin-tools](https://github.com/django-admin-tools/django-admin-tools)
- [x] Custom admin dashboard for index, app index page, autodiscover dashboard from app

#### APIs

- [x] [drf-spectacular](https://github.com/tfranzel/drf-spectacular) - Sane and flexible OpenAPI 3 schema generation for Django REST framework.

#### Commands

- [x] [django-extensions](https://github.com/django-extensions/django-extensions/) - Custom management extensions, notably `runserver_plus` and `shell_plus`.

#### Configuration

- [x] [environs](https://github.com/sloria/environs) - Simplified environment variable parsing that comes with a [Django helper](https://github.com/sloria/environs#usage-with-django) that installs additional packages.

#### General

- [x] [django-filter](https://github.com/carltongibson/django-filter) - Powerful filters based on Django QuerySets.

#### Model Fields

- [x] [django-model-utils](https://github.com/jazzband/django-model-utils) - Django model mixins and utilities.

#### Static Assets

- [x] [whitenoise](https://github.com/evansd/whitenoise) - Simplified static file serving for Python websites.

#### Task Queues

- [x] [django-redis](https://github.com/niwinz/django-redis) - Full-featured Redis cache backend for Django.
- [x] [celery](https://github.com/celery/celery) - Robust and broker-agnostic task queues for bigger, performance-focused projects.
- [x] [flower](https://github.com/mher/flower) - Flower is a web-based tool for monitoring and administrating Celery clusters.
- [x] [django-celery-beat](https://github.com/celery/django-celery-beat) - A periodic task scheduler with database configured by Django's Admin Panel.

#### Testing

- [x] [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar/) - Configurable panels to debug requests/responses.
- [x] [pytest-django](https://github.com/pytest-dev/pytest-django) - Use pytest features in Django.
- [x] [factory-boy](https://github.com/FactoryBoy/factory_boy) - Test fixtures replacement.

#### URLs

- [x] [dj-database-url](https://github.com/jacobian/dj-database-url) - Database URLs.

#### Users

- [x] Comes with custom user model ready to go
- [x] [django-allauth](https://github.com/pennersr/django-allauth/) - Improved user registration including social auth.

### Python Packages

_A short list of Python packages that implement support project._

- [x] Integration with [black](https://github.com/psf/black) - Uncompromising Python code formatter.
- [x] Integration with [pillow](https://github.com/python-pillow/Pillow) - Python Imaging Library.
- [x] Integration with [pytest](https://github.com/pytest-dev/pytest/) - Testing framework.
- [x] Integration with [Mailpit](https://github.com/axllent/mailpit/) for local email testing
- [x] Integration with [Sentry](https://sentry.io/welcome/) for error logging

### Frontend

- [x] Custom static build using Gulp
- [x] Apply [Oswald](https://keenthemes.com/products/oswald-html-free) - Free HTML template from Keen Themes

### Other

- [x] Default integration with [pre-commit](https://github.com/pre-commit/pre-commit) for identifying simple issues before submission to code review
- [x] Docker support using [docker-compose](https://github.com/docker/compose) for development and production (using [Traefik](https://traefik.io/) with [LetsEncrypt](https://letsencrypt.org/) support)

## Support this Project!

This project is an open source project run by volunteers. You can sponsor us via [GitHub Sponsors](https://github.com/sponsors/riso-tech):

Bin Nguyễn, Project Lead ([GitHub](https://github.com/riso-tech)): expertise in Django.

## Special Thanks!

##### [Django Cookiecutter](https://github.com/cookiecutter/cookiecutter-django)

##### [Keen Themes Team](https://keenthemes.com/): [Template Oswald](https://keenthemes.com/products/oswald-html-free)

    Thank you to KeenThemes for granting us a custom license to use their amazing Template Oswald for Django-Awesome UI

    KeenThemes HTML/CSS/JS components are allowed for use only within the Django-Awesome product
    and restricted to be used in a resealable HTML template that can compete with KeenThemes products anyhow.

    The Django-Awesome UI (HTML, CSS and JS components) based on this theme is allowed for use only within the Django-Awesome product
    and therefore cannot be used in derivative works/products without an explicit grant from the Riso Tech Team.
