import os

from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = "ya+&ticzgynvm*y10*f2ldz(v7yoa1!-$=j3!9dk*73hjp@+^k"
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "aa_intercom",
    "test_project",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
]

WSGI_APPLICATION = "test_project.wsgi.application"

DATABASES = {
    "default": {
        "NAME": ":memory:",
        "ENGINE": "django.db.backends.sqlite3",
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]
AUTH_USER_MODEL = "test_project.UserModel"

USE_TZ = True

TEST_RUNNER = "django.test.runner.DiscoverRunner"

SKIP_INTERCOM = True
INTERCOM_ID_PREFIX = ""
INTERCOM_API_ACCESS_TOKEN = "foo"
INTERCOM_EVENT_TYPES = (
    ("example", _("Example Type")),
    ("generic", _("Generic Type"))
)


ENV_PREFIX = "demo-local"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

CELERY_APP_PATH = "app.celery"
CELERY_TASK_ALWAYS_EAGER = True
CELERY_BROKER_URL = ""
CELERY_WORKER_POOL_RESTARTS = True
CELERY_TASK_IGNORE_RESULT = True
CELERY_RESULT_BACKEND = "amqp"
CELERY_TASK_EAGER_PROPAGATES = True

TESTING = True
