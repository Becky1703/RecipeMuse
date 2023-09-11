""" Database """
from . import db
from sqlalchemy.sql import func
from flask_login import UserMixin

class Recipe(db.Model):
    """ Stores recipe data in the database """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    __table_args__ = (
        db.UniqueConstraint('user_id', 'name', name='unique_user_recipe'),
    )
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(255))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    """ Stores User data in the database """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), unique=True, nullable=False)
    recipe = db.relationship('Recipe')

class SavedRecipe(db.Model):
    """ Stores saved recipes data in the database """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    recipe_id = db.Column(db.Integer, nullable=False)



   