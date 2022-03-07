from appname.models.user import User
from appname.models.permission import Permission
from appname.database import db_session
from appname.utils import login_required
from flask import Blueprint, render_template, session

dashboard_controller = Blueprint('dashboard_controller', __name__, template_folder="../../views/dashboard", static_folder="../../static", url_prefix="/dashboard")

@dashboard_controller.route("/", methods=["GET"])
@login_required
def dashboard():
    user = db_session.query(User).filter(User.id == session['user']).first()
    permission = db_session.query(Permission).filter(Permission.id == user.permission).first()
    return render_template('dashboard.html', email=user.email, permission=permission.description)
    