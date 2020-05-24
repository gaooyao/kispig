# coding = utf-8
from flask import jsonify, session
from flask_login import login_user
from models import User
import hashlib


def user_login(request):
    if request.form['username'] and request.form['password']:
        user = User.query.filter(User.username == request.form['username'], User.password_hash == hashlib.sha256(
            request.form['password'].encode("utf8")).hexdigest()).first()
        if user:
            login_user(user)
            session['user'] = request.form['username']
            return jsonify({'status': 'ok', 'info': '%s登录成功' % request.form['username']})
    return jsonify({'status': 'fail', 'info': '%s登录失败' % request.form['username']}), 400
