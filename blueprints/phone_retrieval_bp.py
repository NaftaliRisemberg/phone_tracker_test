from flask import jsonify, current_app, Blueprint
import logging

from services.phone_retrieval_service import GetPhoneRepository

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

@get_phone_bp.route('/find_stronger_than_-60', methods=['GET'])
def find_stronger_interaction():
   try:
      repo = GetPhoneRepository(current_app.neo4j_driver)
      data = repo.find_stronger_interaction()

      return jsonify(data), 200

   except Exception as e:
      print(f'Error in POST /api/phone_tracker: {str(e)}')
      logging.error(f'Error in POST /api/phone_tracker: {str(e)}')
      return jsonify({'error': 'internal server error'}), 500
