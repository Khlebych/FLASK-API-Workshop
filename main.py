import json
from model.twit import Twit
from flask import Flask, jsonify, request
from urllib import request

twits = []

app = Flask(__name__)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Twit):
            return dict(body=o.body, author=o.author)
        else:
            return super().default(o)


app.json_encoder = CustomJSONEncoder


@app.route("/ping", methods=['GET'])
def ping():
    return jsonify({'response': 'pong'})



@app.route('/twit', methods=['POST'])
def create_twit():
    """{"body":"Hello World","author":"@aqaguy"}"""
    twit_json = request.get_json()
    twit = Twit(twit_json['body'], twit_json['author'])
    twits.append(twit)
    return jsonify({'status': 'success'})


@app.route("/twit", methods=['GET'])
def read_twits():
    return jsonify({'twits': [twit.__dict__ for twit in twits]})


if __name__ == '__main__':
    app.run(debug=True)
