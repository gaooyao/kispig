# coding = utf-8

from config import app
import route
from models import User, db

app.run(host=app.config['HOST'], port=app.config['PORT'], debug=False)
