
from flask import Flask, render_template, request, redirect, jsonify, g
import flask_login
import pymysql
import pymysql.cursors
from pprint import pprint as print
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from dynaconf import Dynaconf
#import PIL
#import cv2
#import numpy as np
#from sklearn.model_selection import train_test_split # as something ez to write pls
#import tensorflow as tf
#import tensorflow_hub as hub
#import os
#import matplotlib.pyplot as pplt
#import matplotlib.image as ppltimg
######


app = Flask(__name__)
auth = HTTPBasicAuth()


######userlogin



app = Flask(__name__)
auth = HTTPBasicAuth()

def connect_db():
    return pymysql.connect (
        database = "kick_insight",
        user = "cscarlett",
        password = "228941274",
        host = "10.100.33.60",
        cursorclass = pymysql.cursors.DictCursor,
        autocommit=True
)

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


######userlogin

app.secret_key = "br3@D_y_-19!"
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User:
     
     is_authenticated = True
     is_anonymous = False
     is_active = True

     def __init__(self, id, pfp, email, username):
          
          self.id = id
          self.pfp = pfp
          self.email = email
          self.username = username

     def get_id(self):
          
          return str(self.id)


######

app.secret_key = "br3@D_y_-19!"
login_manager = flask_login.LoginManager()
login_manager.init_app(app)


class User:
   
    is_authenticated = True
    is_anonymous = False
    is_active = True


    def __init__(self, id, pfp, email, username):
        
         self.id = id
         self.pfp = pfp
         self.email = email
         self.username = username


    def get_id(self):
        
         return str(self.id)




######


@login_manager.user_loader


def load_user(user_id):
   
   cursor = get_db().cursor()


   cursor.execute(f"(SELECT * FROM `users` WHERE `id` = {user_id})")


   check = cursor.fetchone()


   cursor.close()


   get_db().commit()


   if check is None:
       
       return None
  
   return User(check["id"], check ["pfp"], check["email"], check["username"])
   
######routs


@app.route("/", methods=["POST", "GET"])
def index():


    return render_template ("homepage.html.jinja")


@app.route("/itempage", methods=["POST", "GET"])
def itempage():
          
    cursor = get_db().cursor()


    cursor.execute(f"GET`*` FROM `products`")


    cursor.close()
    get_db.commit()
    
   
   return render_template("itempage.html.jinja" Products = Products)




@app.route("/signup", methods=["POST", "GET"])
def signup():


   if request.method == "POST":


       newUserEmail = request.form["Email"]


       newUserUsername = request.form["Username"]


       newUserPassword = request.form["Password"]


      
       cursor = get_db().cursor()


       cursor.execute(f"INSERT INTO `Users` (`Email`, `Username`, `Password`) VALUES ('{newUserEmail}', '{newUserUsername}', '{newUserPassword}')")


       cursor.close()


       get_db().commit()


       return redirect("signin.html.jinja")


   return render_template ("signup.html.jinja")






@app.route("/signin", methods=["POST", "GET"])
def signin():


         return render_template("signin.html.jinja")


@app.route("/aipage", methods=["POST", "GET"])
def aipage():


         return render_template("aipage.html.jinja")
@app.route("/cartpage", methods=["POST", "GET"])
def cartpage():


         return render_template("cartpage.html.jinja")


@app.route("/loaditem/<int:name>")
def loaditem(name):
          
  
    cursor = get_db().cursor()


    cursor.execute(f"GET`id`,`name`,`img`,`price`")


    cursor.close()
    get_db.commit()
    return render_template("itempage.html.jinja")