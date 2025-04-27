# DataService/app/routes/healthdata.py

from flask import Blueprint, jsonify

healthdata_bp = Blueprint('healthdata', __name__)

@healthdata_bp.route('/', methods=['GET'])
def index():
    return jsonify({"message": "HealthData API running"}), 200
