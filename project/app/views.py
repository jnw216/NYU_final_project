from app import app, db
from flask import request, render_template,redirect, url_for
import json
from app.models import *

@app.route("/blog",methods=["GET","POST"])
def blog():
    #we want people to be able to comment on our posts.
    return render_template("blog.html")

@app.route("/add", methods=["POST"])
def add_entry():
    #add session test
    #db = get_db()
    #db.execute('insert into entries (title, text) values (?,?)',
    #           [request.form['title'], request.form['text']])
    #db.commit()
    flash('New entery was successfully posted')
    return redirect(url_for('blog'))

@app.route("/resume",methods=["GET"])
def resume():
    #we are going to be returning a PDF
    #OR a very stylized html page
    #OR we could do both
    return render_template()

@app.route("/about_me", methods=["GET"])
def about_me():
    return render_template("about_me.html")

@app.route("/",methods=["GET","POST"])
def index():
    #you want to allow people to contact you from the website
    return render_template("index.html")

@app.route("/analytics",methods=["GET","POST"])
def analytics():
    return render_template("analytics.html")
