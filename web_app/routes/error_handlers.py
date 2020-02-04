
from flask import Blueprint, jsonify

error_handlers = Blueprint('error_handlers', __name__)

@error_handlers.errorhandler(400)
def bad_request(message="Bad Request"):
    response = jsonify({"status": 400, "message": message})
    response.status_code = 400
    return response

@error_handlers.errorhandler(404)
def not_found(message="Not Found"):
    response = jsonify({"status": 404, "message": message})
    response.status_code = 404
    return response
