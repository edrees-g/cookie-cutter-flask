from appname.extensions import bcrypt
from appname.database import db_session
from appname.models.user import User
from appname.utils import logout_required, EMAIL_REGEX
from flask import Blueprint, request, session, render_template, flash, redirect, url_for

signin_controller = Blueprint("signin_controller", __name__, template_folder="../views", static_folder="../static", url_prefix="/signin")

@signin_controller.route("/", methods=["GET", "POST"])
@logout_required
def signin():
    if request.method == "GET":
        return render_template('signin.html', title='Sign In')
    else:
        email = request.form.get('email')
        if (email == None) or (not EMAIL_REGEX.match(email)):
            flash('Email or password incorrect!', 'danger')
            return render_template('signin.html')
        
        password = request.form.get('password')
        if not password:
            flash('Email or password incorrect!', 'danger')
            return render_template('signin.html')
        
        user = db_session.query(User).filter(User.email == email).first()
        if not user:
            flash('Email or password incorrect!', 'danger')
            return render_template('signin.html')
        
        password_hash = user.password
        if not bcrypt.check_password_hash(password_hash, password):
            flash('Email or password incorrect!', 'danger')
            return render_template('signin.html')
        
        # remember me will only be a part of the request form if it has been checked
        # i.e., ImmutableMultiDict([('email', 'example@example.com'), ('password', 'password')])
        # i.e., ImmutableMultiDict([('email', 'example@example.com'), ('password', 'password'), ('remember_me', 'True')])
        session['user'] = user.id
        if request.form.get('remember_me'):
            session.permanent = True
        else:
            session.permanent = False
        
        return redirect(url_for('dashboard_controller.dashboard'))
