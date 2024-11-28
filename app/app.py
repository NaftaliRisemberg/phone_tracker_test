from flask import Flask, jsonify
from blueprints import phone_bp
import logging

app = Flask(__name__)

app.register_blueprint(phone_bp, url_prefix='/api')

app.config['DEBUG'] = True
app.config['LOGGING_LEVEL'] = logging.DEBUG

@app.route('/', methods=['GET'])
def work_check():
    return jsonify('helo world')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

