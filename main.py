from flask import Flask, render_template, request, redirect, jsonify, g
import gpt_2_simple as gpt2
import flask_login
import pymysql
import pymysql.cursors
from pprint import pprint as print
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import Dynaconf

######

app = Flask(__name__)
auth = HTTPBasicAuth()

"""
settings = Dynaconf {
    settings
}
"""


######

def connect_db():
    return pymysql.connect (
        database = "kick_insight",
        user = "cscarlett",
        password = "228941274",
        host = "10.100.33.60",
        cursorclass = pymysql.cursors.DictCursor,
        autocommit=True
)

'''

def get_db():
    #Opens a new database connection per request.        
    if not hasattr(g, 'db'):
        g.db = connect_db()
    return g.db   

@app.teardown_appcontext
def close_db(error):
    #Closes the database connection at the end of request.    
    if hasattr(g, 'db'):
        g.db.close() 

######

@app.route("/", methods=["POST", "GET"])
def index():
    
    if flask_login.current_user.is_authenticated:
         
        return redirect ("/feed")

    return render_template ("home.html.jinja")

@app.route("/register", methods=["POST", "GET"])
def signup():

@app.route("/signin", methods=["POST", "GET"])
def signin():

'''

@app.route("/", methods=["POST", "GET"])
def index():
    
    return render_template ("landing.html.jinja")
