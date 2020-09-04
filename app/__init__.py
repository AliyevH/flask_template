from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from flask_validation import Validator
from flask_redis import FlaskRedis
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
jwt = JWTManager(app)
redis_client = FlaskRedis(app)
Validator(app)

from app import routes, models
