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
ASSET_REPO="AlanOC123/assessment-3-assets-repo"
ASSET_VERSION="@v1.0.2"
ASSET_ORIGIN=f"https://cdn.jsdelivr.net/gh/{ASSET_REPO}{ASSET_VERSION}"