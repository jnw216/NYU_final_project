"""
Here the models for our database is defined.

I am using Postgres, Flask-SQLAlchemy for this application.

For an introduction to Flask-SQLAlchemy check out: http://flask-sqlalchemy.pocoo.org/2.1/

__init__ function for each model is a constructor, and is necessary to enter
""" 
from app import db
from datetime import datetime
import hashlib
class User(db.Model):
	"""
	"""
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.String,unique=True)
	password = db.Column(db.String)

	def __init__(self,user_id,password):
		self.user_id = user_id
		self.password = hashlib.sha256(password.encode("utf-8")).hexdigest()