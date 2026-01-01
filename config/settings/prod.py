from .base import *

DEBUG = False
ALLOWED_HOSTS = ["todo-project4-clean.onrender.com"]

SECRET_KEY = os.getenv("SECRET_KEY")

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]

CSRF_TRUSTED_ORIGINS = [
    "https://todo-project4-clean.onrender.com",
]

# Whitenoise用の設定
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
