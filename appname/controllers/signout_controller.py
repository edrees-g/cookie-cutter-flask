from appname.utils import login_required
from flask import Blueprint, flash, redirect, url_for, session

signout_controller = Blueprint("signout_controller", __name__, template_folder="../views", static_folder="../static", url_prefix="/signout")

@signout_controller.route("/", methods=["GET"])
@login_required
def signout():
    session.clear()
    flash("You have been successfully signed out!", 'success-signout')
    return redirect(url_for('signin_controller.signin'))
    