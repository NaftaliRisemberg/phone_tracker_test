from flask import Flask, jsonify
from blueprints.phone_retrieval_bp import get_phone_bp
from blueprints.data_mange_bp import phone_bp
from db_conifg.init_db import init_neo4j
import logging

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['LOGGING_LEVEL'] = logging.DEBUG

app.register_blueprint(phone_bp, url_prefix='/api')
app.register_blueprint(get_phone_bp, url_prefix='/api')

with app.app_context():
    app.neo4j_driver = init_neo4j()

@app.route('/', methods=['GET'])
def work_check():
    return jsonify('helo world')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

