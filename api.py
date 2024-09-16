from flask import Blueprint, jsonify, request

api_bp = Blueprint('api/v1', __name__)

@api_bp.route('/guess', methods=['GET'])
def check_guess():
    return 'test best'