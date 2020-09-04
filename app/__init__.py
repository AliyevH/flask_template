import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import (JWTManager, jwt_required, create_access_token, get_jwt_identity)
from flask_validation import Validator
from flask_redis import FlaskRedis
from core.settings import Development, Production
from flask_migrate import Migrate


if os.getenv("ENV_SETTINGS") == "development":
    config = Development
elif os.getenv("ENV_SETTINGS") == "production":
    config = Production


app = Flask(__name__)
app.config.from_object(config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)
redis_client = FlaskRedis(app)
Validator(app)

from app import routes, models
