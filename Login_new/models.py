# -*- encoding=UTF-8 -*-

from Login_new import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return ('<User %d %s>' % (self.id, self.username)).encode('gbk')