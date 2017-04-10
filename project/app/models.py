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
    visit_time_id = db.Column(db.Integer, db.ForeignKey('visit_time.id'))
	
    def __init__(self,user_id,password):
        self.user_id = user_id
        self.password = password

class BlogEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry_name = db.Column(db.String)
    entry = db.Column(db.String)
    timestamp = db.Column(db.DateTime)

    def __init__(self,entry_name,entry,timestamp):
        self.entry_name = entry_name
        self.entry = entry
        self.timestamp = timestamp

class PageViews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    page_views = db.Column(db.Integer)
    page_name = db.Column(db.String)

    def __init__(self,page_views, page_name):
        self.page_views = page_views
        self.page_name = page_name

class IPAnalytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String)
    page_views = db.Column(db.Integer)
        
    def __init__(self,ip_address, page_views):
        self.ip_address = ip_address
        self.page_views = page_views

class ActiveConnections(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    active_connections = db.Column(db.Integer)

    def __init__(self,active_connections):
        self.active_connections = active_connections

class VisitTime(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    visit_time = db.Column(db.Float)
    page_name = db.Column(db.String)
    user = db.relationship('User', backref='visit_time',
                           lazy='dynamic')


