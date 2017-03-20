from flask import Flask, render_template
import random
from datetime import datetime
app = Flask(__name__)

def check_if_afterwork():
    if datetime.now().hour > 18:
        return True
    else:
        return False

@app.route("/",methods=["GET","POST"])
def index(): 
    return render_template("index.html",thing=random.randint(0,100), after_6pm=check_if_afterwork())

app.run(debug=True)
