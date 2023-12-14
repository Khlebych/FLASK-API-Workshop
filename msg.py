from user import User


class Msg:

    def __init__(self, msg_id:int, author: User, body: str):
        self.msg_id = msg_id
        self.author = author
        self.body = body
