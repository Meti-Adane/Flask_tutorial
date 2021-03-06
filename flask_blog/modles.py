from flask_blog import db, login_manger
from datetime import datetime
from flask_login import UserMixin

@login_manger.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

    password = db.Column(db.String(60), nullable = False)
    image_file = db.Column(db.String(20), unique = False, nullable = False, default = 'default.jpg')

    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', '{self.password}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title= db.Column(db.String(100), nullable=False, unique = False)
    date_posted=  db.Column(db.DateTime, nullable=False, unique = False, default = datetime.utcnow)
    content= db.Column(db.Text, nullable=False, unique = False)
    user_id=  db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


