from app import app, redis_client, db

from flask import request, jsonify
from flask_validation import json_required, validate_common
from flask_jwt_extended import jwt_required, create_access_token, create_refresh_token, get_jwt_identity, \
    jwt_refresh_token_required


import requests
import datetime

from .models import Test
from .errors import *
from .decorators import custom_decorator

@app.route('/api/v1/auth/refresh/', methods=['POST'])
@jwt_refresh_token_required
def refresh():
    current_user = get_jwt_identity()
    ret = {
        'access_token': create_access_token(identity=current_user, expires_delta=datetime.timedelta(seconds=15 * 60)),
        'refresh_token': create_refresh_token(identity=current_user,
                                              expires_delta=datetime.timedelta(seconds=364 * 30 * 24 * 60 * 60))
    }
    return jsonify(ret), 200

