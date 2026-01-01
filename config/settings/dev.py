from .base import *

DEBUG = True

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")

STATICFILES_DIRS = [BASE_DIR / "static"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
