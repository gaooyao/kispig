# coding = utf-8
from flask import render_template, request
from flask_login import login_required
from config import app
from tools.route import route as tools_route
from user.login import user_login


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test')
@login_required
def test():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    return user_login(request)


@app.route('/tools/<string:fun>', methods=['POST'])
def tools(fun=None):
    return tools_route(request, fun)


@app.errorhandler(404)
def miss(e):
    return render_template('404.html'), 404
