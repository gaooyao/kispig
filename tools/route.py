# coding = utf-8
from tools.send_msg import send_msg
from tools.send_mail import send_mail
from flask_login import login_required


def route(request, fun):
    if fun == 'send-msg':
        return send_msg(request)
    if fun == 'send-mail':
        return send_mail(request)
