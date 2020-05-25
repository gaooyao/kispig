# coding = utf-8
from flask import jsonify, session, redirect
from flask_login import login_user, logout_user, login_required
from models import User
import hashlib


def user_login(request):
    if request.form.get('username') and request.form.get('password'):
        user = User.query.filter(User.username == request.form.get('username'),
                                 User.password_hash == request.form.get('password')).first()
        if user:
            login_user(user)
            session['username'] = request.form.get('username')
            return jsonify({'status': 'ok', 'info': '%s login success.' % request.form.get('username')})
    return jsonify({'status': 'fail', 'info': '%s login fail.' % request.form.get('username')}), 400


@login_required
def user_logout(request):
    logout_user()
    session.pop('username')
    return redirect('/')
