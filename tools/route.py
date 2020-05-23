# coding = utf-8
from tools.send_msg import send_msg
from tools.send_mail import send_mail


def route(fun, req):
    if fun == 'send-msg':
        return send_msg(req)
    if fun == 'send-mail':
        return send_mail(req)
