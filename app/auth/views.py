from flask import render_template,request, redirect, url_for
from . import auth
from app.models import User
from flask_login import login_user,logout_user,current_user

@auth.route("/login",methods=["GET","POST"])
def login():
    errors = []
    if request.method == "POST":
        form = request.form
        username = form.get("username")
        if not username:
            errors.append("Must enter username")
            return render_template("auth/login.html",errors=errors)
        password = form.get("password")
        if not password:
            errors.append("Must enter password")
            return render_template("auth/login.html",errors=errors)
        user =  User.query.filter_by(username=username).first()
        if not user:
            errors.append("User with that username or password does not exist") 
            return render_template("auth/login.html",errors=errors)
        if not user.check_password(password):
            errors.append("User with that username or password does not exist") 
            render_template("auth/login.html",errors=errors)
        login_user(user)
        return redirect(url_for("main.home"))

    return render_template("auth/login.html",errors=errors)

@auth.route("/register", methods=["POST","GET"])
def register():
    errors = []
    if request.method == "POST":
        form = request.form
        username = form.get("username")
        if not username:
            errors.append("Must enter username")
            return render_template("auth/register.html",errors=errors)
        password = form.get("password")
        if not password:
            errors.append("Must enter password")
            return render_template("auth/register.html",errors=errors)
        password_confirm = form.get("password_confirm")
        if not password_confirm:
            errors.append("Must enter password confirm field")
            return render_template("auth/register.html",errors=errors)
        if password_confirm !=  password:
            errors.append("Passwords do not match")
            return render_template("auth/register.html",errors=errors)
        user = User.query.filter_by(username=username).first()
        if user:
            errors.append("User with that username already exists")
            return render_template("auth/register.html",errors=errors)
        user = User(username=username)
        user.set_password(password)
        user.save()
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html",errors=errors)


@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))