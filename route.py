# coding = utf-8
from flask import render_template, request
from config import app
from tools.route import route as tools_route
from user.login import user_login


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST'])
def login():
    return user_login()


@app.route('/tools/<string:fun>/<path:req>')
def tools(fun=None, req=None):
    print(request)
    return tools_route(fun, req)


@app.errorhandler(404)
def miss(e):
    return render_template('404.html'), 404
