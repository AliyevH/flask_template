import os

class Config(object):
    """Base class configuration"""
    DEBUG = True
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

