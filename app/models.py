from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from . import db,admin,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime



@login_manager.user_loader
def load_user(user_id):
 return User.query.get(int(user_id))



class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id =db.Column(db.Integer,primary_key =True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


class Blog(db.Model):

   __tablename__ = 'blogs'

   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(50))
   subtitle = db.Column(db.String(50))
   author = db.Column(db.String(20))
   date_posted = db.Column(db.DateTime, default=datetime.utcnow)
   content = db.Column(db.Text)

admin.add_view(ModelView(User,db.session))
