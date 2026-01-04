from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "todo-project4-clean.onrender.com",
    ".onrender.com",
]

SECRET_KEY = os.getenv("SECRET_KEY")

CSRF_TRUSTED_ORIGINS = [
    "https://todo-project4-clean.onrender.com",
]

# Manifestはいれたらあかん
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

