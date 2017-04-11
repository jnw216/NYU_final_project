from app import app, db
from flask import request, render_template,redirect, url_for, send_from_directory
import json
import os
from app.models import User, BlogEntry
import hashlib
from datetime import datetime

@app.route("/blog",methods=["GET","POST"])
def blog():
    #we want people to be able to comment on our posts.
    return render_template("blog.html", blog_entries=BlogEntry.query.all())

@app.route("/grab_entry/<entry_name>",methods=["GET","POST"])
def grab_entry(entry_name):
    blog_entry = BlogEntry.query.filter_by(entry_name=entry_name).first()
    return render_template("render_entry.html",blog_entry=blog_entry.entry)

@app.route("/write_entry",methods=["GET","POST"])
def write_entry():
    if request.method=="POST":
        #Get something from the user
        title = request.form.get("title")
        body = request.form.get("body")
        #Save it to the database
        blog_entry = BlogEntry(title, body, datetime.now())
        db.session.add(blog_entry)
        db.session.commit()
        #go somewhere else
        return render_template("blog.html",blog_entries=BlogEntry.query.all())
    else:
        return render_template("write_entry.html")

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
    src_dir =  os.path.abspath(os.path.dirname(__file__)) + "/static/"  ##### #/resume.pdf"
    return  send_from_directory(src_dir,'resume.pdf')

@app.route("/about_me", methods=["GET"])
def about_me():
    return render_template("about_me.html")

@app.route("/", methods=["GET","POST"])
def index():
    #you want to allow people to contact you from the website
    return render_template("index.html")

@app.route("/sign_in", methods=["POST"])
def sign_in():
    username = request.form.get("username")
    password_field = request.form.get("password_field")
    user = User.query.filter_by(user_id=username).first()
    if user.password == hashlib.sha256(password_field.encode("utf-8")).hexdigest():
        return render_template("index.html",login_attempt="successful")
    else:
        return render_template("index.html",login_attempt="failure")

@app.route("/sign_up", methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username")
        password_field = request.form.get("password_field")
        password_field = hashlib.sha256(password_field.encode("utf-8")).hexdigest()
        new_user = User(username,password_field)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("index"))
    else:
        return render_template("sign_up.html")
    
@app.route("/analytics",methods=["GET","POST"])
def analytics():
    return render_template("analytics.html")
