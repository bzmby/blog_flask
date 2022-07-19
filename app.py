from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
	return "Blog Home"

#blue print (which is an app) for admin is made mod_admin and is imported below. and should be registered below too: 
from mod_admin import admin


app.register_blueprint(admin)

