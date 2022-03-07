from flask import Blueprint, render_template
from appname.utils import logout_required

home_controller = Blueprint("home_controller", __name__, template_folder="../views", static_folder="../static", url_prefix="/home")

@home_controller.route("/", methods=["GET"])
@logout_required
def home():
    return render_template('home.html')
