from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/ping', methods=['GET'])
def index():
    return jsonify({'response': 'PPOONNGG'})


if __name__ == '__maim__':
    app.run(debug=True)
