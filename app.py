# coding = utf-8

from flask_login import login_manager
from config import app, login_manager
import route
from models import User, db


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter(User.id == user_id).first()


app.run(host=app.config['HOST'], port=app.config['PORT'], debug=False)
