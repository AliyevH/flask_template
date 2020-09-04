from core.settings.base import Config


class Development(Config):
    """Development Environment Configuration Class"""

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/db'