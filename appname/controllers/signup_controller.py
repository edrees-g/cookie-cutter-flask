from appname.extensions import bcrypt
from appname.database import db_session
from appname.models.user import User
from appname.utils import logout_required, EMAIL_REGEX, check_password
from flask import Blueprint, request, redirect, render_template, flash, url_for

signup_controller = Blueprint("signup_controller", __name__, template_folder="../views", static_folder="../static", url_prefix="/signup")

@signup_controller.route("/", methods=["GET", "POST"])
@logout_required
def signup():
    if request.method == "GET":
        return render_template('signup.html', title='signup')
    else:
        email = request.form.get("email")
        if (email == None) or (not EMAIL_REGEX.match(email)):
            flash('Invalid email!', 'danger')
            return render_template('signup.html')
        
        password = request.form.get('password')
        password_complexity_response = check_password(password)
        if password_complexity_response != "PASS":
            flash(password_complexity_response, 'danger')
            return render_template('signup.html')
        
        confirm_password = request.form.get('confirm_password')
        if confirm_password != password:
            flash('Passwords do not match!', 'danger')
            return render_template('signup.html')
        
        if db_session.query(User).filter(User.email == email).first():
            flash('Email already exists!', 'danger')
            return render_template('signup.html')
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(email=email, password=hashed_password)
        db_session.add(user)

        try:
            db_session.commit()
        except Exception as e:
            print(e)
            # TODO: Flask logging
            flash('Oopos something went wrong, please contact us for accistance!', 'danger')
            return render_template('signup.html')
        
        flash('Account successfully created!', 'success-signup')
        return redirect(url_for('signup_controller.signup'))
