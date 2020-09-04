from core.settings.base import Config
import os

class Production(Config):
    """Producition Environment Configuration Class"""

    DEBUG = False

    SECRET_KEY = os.environ.get('SECRET_KEY')

    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION = 'headers'
    JWT_ACCESS_TOKEN_EXPIRES = 15 * 60
    JWT_REFRESH_TOKEN_EXPIRES = 364 * 30 * 24 * 60 * 60

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    
    REDIS_HOST = os.environ.get("REDIS_HOST") or False
    REDIS_PORT = os.environ.get("REDIS_PORT") or False
    REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD") or False

    if REDIS_HOST and REDIS_PASSWORD and REDIS_PASSWORD:
        REDIS_URI = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"