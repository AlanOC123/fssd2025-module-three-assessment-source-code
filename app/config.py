import os
from dotenv import load_dotenv

load_dotenv()

ENV = os.getenv("FLASK_ENV", "development")
SITE_NAME = "PLANET ."
SITE_NAME_ACCESSIBLE = "Planet stop"
SITE_TAGLINE = "Explore worlds, beautifully."
SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-insecure-key")
SESSION_COOKIE_SECURE = ENV == "production"
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE="Lax"
