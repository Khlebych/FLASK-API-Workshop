import json
from msg import Msg
from user import User
from flask import Flask, jsonify, request

msgs = []

users = []

app = Flask(__name__)


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Msg):
            return {'body': o.body, 'author': o.author, 'message id': o.msg_id}

        if isinstance(o, User):
            return {'user_id': o.user_id, 'username': o.username}

        else:
            return super().default(o)


app.json_encoder = CustomJSONEncoder


@app.route("/ping", methods=['GET'])
def ping():
    return jsonify({'response server': 'ping  OK'})


# @app.route('/user', methods=['POST'])
# def create_user():
#     """ {"user_id": 1, "username": "qwerty"} """
#
#     user_json = request.get_json()
#     usr = User(user_json['user_id'], user_json['username'])
#     users.append(usr)
#     return jsonify({'status user:': ' - success'})
#
#
# @app.route("/user", methods=['GET'])
# def read_user():
#     return jsonify({'users': [user.__dict__ for user in users]})


@app.route('/msg', methods=['POST'])
def create_msg():
    """ {"msg_id":1, "author": "@test", "body": "test POST"} """

    msg_json = request.get_json()
    msg = Msg(msg_json['msg_id'], msg_json['author'], msg_json['body'])
    msgs.append(msg)
    return jsonify({'status msg:': ' - success'})


@app.route("/msg", methods=['GET'])
def read_msg():
    return jsonify({'msgs': [msg.__dict__ for msg in msgs]})


@app.route("/msg/<int:msg_id>", methods=['PUT'])
def upd_msg(msg):
    ''' {"msg_id":1", "author": "@test", "body": "test PUT-1"} '''
    msg_json = request.get_json()
    for msg in msgs:
        if msg.msg_id == msg_json.msg_id:
            msg.body = msg_json.body("new message after PUT")
        return jsonify({'msgs': [msg.__dict__ for msg in msgs]})


@app.route("/msg//", methods=['DELETE'])
def deleting_msg(msg_id=None):
#    msg_json = request.get_json()
#    msg_del = User(user_id=user_json['user_id'])
    for msg in msgs:
        if msg.msg_id == msg_id:
            msgs.remove(msg)
        return jsonify({'msgs': [msg.__dict__ for msg in msgs]})


if __name__ == '__main__':
    app.run(debug=True)
