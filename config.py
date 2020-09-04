import os

REDIS_HOST = os.environ.get("REDIS_HOST") or 'localhost'
REDIS_PORT = os.environ.get("REDIS_PORT") or 6379
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD") or 'redis-password'


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or ''
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or ''
    JWT_TOKEN_LOCATION = 'headers'
    JWT_ACCESS_TOKEN_EXPIRES = 15 * 60
    JWT_REFRESH_TOKEN_EXPIRES = 364 * 30 * 24 * 60 * 60

    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'mysql://root:root@localhost/db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"
