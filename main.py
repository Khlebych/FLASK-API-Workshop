import json
from model.twit import Twit
from flask import Flask, jsonify, request
from urllib import request

twits = []

app = Flask(__name__)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(object, Twit):
            return {'body':object.body, 'author':object.author}
        else:
            return super().default(object)


app.json_encoder = CustomJSONEncoder


@app.route("/ping", methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})


@app.route('/twit', methods=['POST'])
def create_twit():
    """{"body":"Hello World","author":"@aqaguy"}"""

    twit_json = request.get_jsonj()
    twit = Twit(twit_json['body'],twit_json['author'])
    twits.append(twit)
    return jsonify({'status':'success'})


@app.route("/twit", methods=['GET'])
def read_twits():
    return jsonify({'twits': twits})


if __name__ == '__maim__':
    app.run(debug=True)
