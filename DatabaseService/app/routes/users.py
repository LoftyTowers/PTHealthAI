from flask import Blueprint, jsonify, request

users_bp = Blueprint('users', __name__)

@users_bp.route('/', methods=['GET'])
def get_users():
    # Placeholder for fetching users from DB
    return jsonify({"message": "List of users"}), 200

@users_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    # Placeholder for inserting a user
    return jsonify({"message": "User created", "user": data}), 201
