from . import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Create a database connection
#db = SQLAlchemy()

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, name, ingredients, instructions, image_url, user_id):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions
        self.image_url = image_url
        self.user_id = user_id

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    recipe = db.relationship('Recipe')


    """def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username"""

    def __init__(self, email, password, username):
        self.email = email
        self.username = username
        self.set_password(password)

    def __repr__(self):
        return '<User %r>' % self.email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.email)
    

def init_db():
    db.create_all()
    #create test user
    #new_user = User('abc@a.com', '12345')
    #new_user.username = 'Lady'
    db.session.add()
    db.session.commit()

if __name__ == "__main__":
    init_db()