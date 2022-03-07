from appname.utils import logout_required
from flask import Blueprint, render_template

about_controller = Blueprint("about_controller", __name__, template_folder="../views", static_folder="../static", url_prefix="/about")

@about_controller.route("/", methods=["GET"])
@logout_required
def about():
    return render_template('about.html', title='About')
