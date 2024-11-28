from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def work_check():
    return jsonify('helo world')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

