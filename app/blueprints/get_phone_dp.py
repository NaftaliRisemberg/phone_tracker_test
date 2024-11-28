from flask import request, jsonify, current_app, Blueprint
import logging
from .gey_phone_service import GetPhoneRepository

get_phone_bp = Blueprint('get_phone_bp', __name__)

@get_phone_bp.route('/find_bluetooth_connections', methods=['GET'])
def find_bluetooth_connections():
   try:
      repo = GetPhoneRepository(current_app.neo4j_driver)
      data = repo.find_bluetooth_connections()

      return jsonify(data), 200

   except Exception as e:
      print(f'Error in POST /api/phone_tracker: {str(e)}')
      logging.error(f'Error in POST /api/phone_tracker: {str(e)}')
      return jsonify({'error': 'internal server error'}), 500

