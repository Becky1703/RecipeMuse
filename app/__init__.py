""" Initializes the application and configures the database """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    """ Database configuration """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abcd'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://recipemuse_dev:recipemuse_pwd@localhost/recipemuse_db"
    
    db.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from .views import views
    from .auth import auth

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')


    # This is needed for database session calls (e.g. db.session.commit)
    with app.app_context():
      try:
          db.create_all()
      except Exception as exception:
          print("got the following exception when attempting db.create_all() in __init__.py: " + str(exception))
      finally:
          print("db.create_all() in __init__.py was successfull - no exceptions were raised")
    from .models import User
 

    @login_manager.user_loader
    def load_user(user_id):
        """ Callback used to reload the user object from the user ID stored in the session """
        return User.query.get(int(user_id))
    
    return app
