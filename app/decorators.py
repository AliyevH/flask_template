from functools import wraps

from flask import abort, current_app, request, jsonify


def custom_decorator():
    """
    A decorators
    """

    @wraps()
    def wrapper(*args, **kwargs):
        try:
            json_data = request.get_json()
            return jsonify({'msg': 'Custom msg'}), 200
        except Exception as e:
            print(str(e))
            return jsonify({'msg': 'Custom msg'}), 400

    return wrapper
