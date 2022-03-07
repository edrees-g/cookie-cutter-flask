from appname.database import db_session
from appname.models.user import User
from flask import Blueprint, session, render_template

contact_controller = Blueprint("contact_controller", __name__, template_folder="../views", static_folder="../static", url_prefix="/contact")

@contact_controller.route("/", methods=["GET", "POST"])
def contact():
    if 'user' in session:
        user = db_session.query(User).filter(User.id == session['user']).first()
        return render_template('contact.html', title='Contact Us', email=user.email)
    return render_template('contact.html', title='Contact Us')
    