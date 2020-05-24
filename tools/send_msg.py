# coding = utf-8

import re
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from flask import session, jsonify
import config

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest


def send_msg(request):
    if not request.form.get('receiver') or not re.match(r"^1[35678]\d{9}$", request.form.get('receiver')):
        return jsonify({'status': 'fail', 'info': 'send msg fail, please check receiver.'}), 400
    else:
        receiver = request.form.get('receiver')
    if not request.form.get('text') or not re.match(r"^\d{6}$", request.form.get('text')):
        return jsonify({'status': 'fail', 'info': 'send msg fail, please check text.'}), 400
    else:
        text = request.form.get('text')
    if not session.get('user') and request.form.get('token') != config.Config.TOKEN:
        return jsonify({'status': 'fail', 'info': 'no certified operate.'}), 400

    try:
        client = AcsClient(config.Config.ALI_ASSESS_KEY_ID, config.Config.ALI_ASSESS_KEY_SECRET,
                           config.Config.ALI_REGION_ID)
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https')
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')

        request.add_query_param('RegionId', config.Config.ALI_REGION_ID)
        request.add_query_param('PhoneNumbers', receiver)
        request.add_query_param('SignName', "KisPig网")
        request.add_query_param('TemplateCode', "SMS_184215625")
        request.add_query_param('TemplateParam', "{\"message\": \"" + text + "\"}")
        response = client.do_action_with_exception(request)
        return jsonify({'status': 'ok', 'info': 'send msg success.'}), 200
    except Exception as e:
        return jsonify({'status': 'fail', 'info': 'send msg fail.', 'reason': str(e)}), 400
