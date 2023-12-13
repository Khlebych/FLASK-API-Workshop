import json
from msg import Msg
from flask import Flask, jsonify, request


msgs = []

app = Flask(__name__)


class CustomJSONEncoder(json.JSONEncoder):
   def default(self, o):
       if isinstance(o, Msg):
           return {'body':o.body, 'author':o.author}
       else:
           return super().default(o)

app.json_encoder = CustomJSONEncoder

@app.route("/ping", methods=['GET'])
def ping():
   return jsonify({'response': 'pong'})

@app.route('/msg', methods=['POST'])
def create_msg():
   """{"body":"Hello World","author":"@aqaguy"}"""

   msg_json = request.get_json()
   msg = Msg(msg_json['body'], msg_json['author'])
   msgs.append(msg)
   return jsonify({'status':'success'})


@app.route("/msg", methods=['GET'])
def read_msgs():
   return jsonify({'msgs': [msg.__dict__ for msg in msgs]})


if __name__ == '__main__':
   app.run(debug=True)
