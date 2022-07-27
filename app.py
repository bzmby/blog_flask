from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Development   #since we are developing now, we use development now
from flask_migrate import Migrate
#if you want to change sth in one of the classes in the model.py use flask migrate


app = Flask(__name__)
app.config.from_object(Development)

db = SQLAlchemy(app)
migrate = Migrate(app, db) #it takes app and db instance


@app.route('/')
def index():
	return "Blog Home"


#blue print (which is an app) for admin is made mod_admin and is imported below. and should be registered below too: 
from mod_admin import admin
from mod_users import users


app.register_blueprint(admin)
app.register_blueprint(users)




