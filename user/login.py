# coding = utf-8
from flask import request
from flask_login import login_user
from models import User
import hashlib


def user_login():
    import pdb
    pdb.set_trace()
    user = User.query.filter(User.username == request.form['username'], User.password_hash == hashlib.sha256(
        request.form['password'].encode("utf8")).hexdigest()).first()
    if user:
        login_user(user)
        return 'login success'
    return 'login fail'
