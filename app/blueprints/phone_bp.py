from flask import request, jsonify, current_app, Blueprint
from .phone_service import PhoneRepository
import logging

phone_bp = Blueprint('phone_bp', __name__)

@phone_bp.route("/phone_tracker", methods=['POST'])
def get_interaction():
   data = request.get_json()
   try:
      repo = PhoneRepository(current_app.neo4j_driver)
      interaction = repo.create_phone_interaction(data)

      return jsonify({
         'status': 'success',
         'interaction': interaction
      }), 201

   except Exception as e:
      print(f'Error in POST /api/phone_tracker: {str(e)}')
      logging.error(f'Error in POST /api/phone_tracker: {str(e)}')
      return jsonify({'error': 'internal server error'}), 500







