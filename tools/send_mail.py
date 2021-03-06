# coding = utf-8

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from flask import session, jsonify
import config


def send_mail(request):
    if not request.form.get('receiver'):
        return jsonify({'status': 'fail', 'info': 'send mail fail, because no receiver.'}), 400
    else:
        receiver = request.form.get('receiver')
    if not request.form.get('title'):
        return jsonify({'status': 'fail', 'info': 'send mail fail, because no title.'}), 400
    else:
        title = request.form.get('title')
    if 'username' not in session and request.form.get('token') != config.Config.TOKEN:
        return jsonify({'status': 'fail', 'info': 'no certified operate.'}), 400
    try:
        context = request.form.get('context') if request.form.get('context') else ''
        context = context.encode().decode('utf-8')
        msg = MIMEText(context, 'plain', 'utf-8')
        msg['Subject'] = Header(title, 'utf-8')
        msg['From'] = config.Config.APP_NAME
        msg['To'] = receiver
        smtp = smtplib.SMTP()
        smtp.connect(config.Config.MAIL_SMTP_SERVER)
        smtp.login(config.Config.MAIL_USER_NAME, config.Config.MAIL_PASSWORD)
        smtp.sendmail(config.Config.MAIL_SENDER, receiver, msg.as_string())
        smtp.quit()
        return jsonify({'status': 'ok', 'info': 'mail send success.'}), 200
    except Exception as e:
        return jsonify({'status': 'fail', 'info': 'mail send fail.', 'reason': str(e)}), 400
