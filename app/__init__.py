from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from .models import db
import logging


db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)


    # Set the logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logging.basicConfig(level=logging.DEBUG)

    # Optionally, write logs to a file
    file_handler = logging.FileHandler("app.log")
    file_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(file_handler)


    app.config['SECRET_KEY'] = 'abcd'
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://recipemuse_dev:recipemuse_pwd@localhost/recipemuse_db"
    #app.config["SQLALCHEMY_ECHO"] = True
    #app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    #login_manager.init_app(app)
    #login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    
    from .views import views
    from .auth import auth

    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(views, url_prefix='/')


     # this is needed in order for database session calls (e.g. db.session.commit)
    with app.app_context():
      try:
          db.create_all()
      except Exception as exception:
          print("got the following exception when attempting db.create_all() in __init__.py: " + str(exception))
      finally:
          print("db.create_all() in __init__.py was successfull - no exceptions were raised")
    from .models import User, Recipe
 
       
    #from .models import User, Recipe

    #with app.app_context():
    #   db.create_all()


    #login_manager = LoginManager(app)
    #login_manager.login_view = 'auth.login'
    #login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    
    return app
