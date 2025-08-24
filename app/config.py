import os

SITE_NAME = "PLANET ."
SITE_NAME_ACCESSIBLE = "Planet stop"
SITE_TAGLINE = "Explore worlds, beautifully."
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-insecure-key")
SESSION_COOKIE_SECURE = os.getenv("FLASK_ENV") == "production"
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE="Lax"
