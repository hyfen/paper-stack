import os
ROOT_URLCONF = 'urls'  # Replace 'project.urls' with just 'urls'

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.doc.XViewMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.sites',
)

ROOT_PATH = os.path.dirname(__file__)
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or
    # "C:/www/django/templates".  Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    ROOT_PATH + '/templates',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media")