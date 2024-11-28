from flask import Blueprint, request, jsonify, current_app

phone_bp = Blueprint('phone_bp', __name__)

@phone_bp.route("/api/phone_tracker", methods=['POST'])
def get_interaction():
   print(request.json)
   return jsonify({ }), 200
