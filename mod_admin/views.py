from flask import session
from . import admin


@admin.route('/')
def index():
	return "hello from admin index"




@admin.route('/login/')
def login():
	session['name'] = 'behzad'
	print(session.get('name'))
	print(session)
	return '1'

