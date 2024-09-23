from flask import Blueprint, jsonify, request

api = Blueprint('api/v1', __name__)

@api.route('/guess', methods=['GET'])
def check_guess():
    return 'test best'

@api.route('/scoreboard', methods=['GET'])
def get_scoreboard():
    return 'score'

@api.route('/name/<name>', method=['POST'])
def set_name(name):
    return name

@api.route('/name/<id>', method=['GET'])
def get_name(id):
    return 'name'