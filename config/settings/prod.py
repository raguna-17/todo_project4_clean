from .base import *

DEBUG = True

ALLOWED_HOSTS = ["todo-project4-clean.onrender.com"]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

SECRET_KEY = os.getenv("SECRET_KEY")


CSRF_TRUSTED_ORIGINS = [
    "https://todo-project4-clean.onrender.com",
]
