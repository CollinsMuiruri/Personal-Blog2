from flask import render_template, request, redirect, url_for, abort
from . import auth
from flask_login import login_required,current_user,login_user,logout_user
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db


@auth.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash('Invalid username or Password')

    title = "Login page"
    return render_template('auth/login.html',login_form = login_form,title=title)
