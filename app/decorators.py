from functools import wraps

from flask import abort, current_app, request, jsonify


def custom_decorator(func):
    """
    A decorators
    """
    return "wrapper"