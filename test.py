from app import db
from models import User

u = User(username='admin', email='admin@example.com',
         password_hash='b3282a2f2a28757b3a18ab833de16a9c54518c0b0cf493e3f0a7cf09386f326a')
db.session.add(u)
db.session.commit()



