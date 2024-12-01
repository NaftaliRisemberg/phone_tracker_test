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
      print(f'Error in GET /api/phone_tracker: {str(e)}')
      logging.error(f'Error in GET /find_bluetooth_connections: {str(e)}')
      return jsonify({'error': 'internal server error'}), 500

@get_phone_bp.route('/find_stronger_than_-60', methods=['GET'])
def find_stronger_interaction():
   try:
      repo = GetPhoneRepository(current_app.neo4j_driver)
      data = repo.find_stronger_interaction()

      return jsonify(data), 200

   except Exception as e:
      print(f'Error in GET /api/find_stronger_than_-60: {str(e)}')
      logging.error(f'Error in GET /api/find_stronger_than_-60: {str(e)}')
      return jsonify({'error': 'internal server error'}), 500

@get_phone_bp.route('/find_count_by_sender_id', methods=['GET'])
def find_count_by_sender_id():
   try:
      sender_id = request.args.get('id')

      if sender_id is None:
         return jsonify({'error': 'Missing sender_id parameter'}), 400

      repo = GetPhoneRepository(current_app.neo4j_driver)
      data = repo.find_count_by_sender_id()

      return jsonify(data), 200

   except Exception as e:
      print(f'Error in GET /api/find_count_by_sender_id: {str(e)}')
      logging.error(f'Error in GET /find_count_by_sender_id: {str(e)}')
      return jsonify({'error': 'internal server error'}), 500