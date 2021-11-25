from flask import Blueprint, render_template, jsonify, request, redirect, session, url_for
from . import nickname
import functools
from .models import db
import re
import bcrypt

def login_required(func):
    @functools.wraps(func)
    def wrapped_view(**kwargs):
        user = session.get('user_email')
        if user:
            return redirect(url_for('index'))
        return func(**kwargs)

    return wrapped_view

login = Blueprint("login", __name__)

@login.route("/login-join", methods=["GET","POST"])
@login_required
def get_login():
    if request.method == "GET":
        return render_template('login-join.html')
    else:
        email = request.form.get("user_email")
        pw = request.form.get("user_pw")
        user = db.User_collection.find_one({"User_email":email})
        if bcrypt.checkpw(pw.encode('utf-8'),user["User_pw"].encode('utf-8')):
            session['user_email'] = email
            return redirect(url_for('feed.get_feed'))
        else:
            return redirect(url_for('login.get_login'))

@login.route("/logout")
def get_logout():
    session.pop('user_email',None)
    return redirect(url_for('intro.get_intro'))

    


