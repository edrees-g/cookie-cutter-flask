from crypt import methods
from flask import Blueprint, redirect, url_for

root_controller = Blueprint('root_controller', __name__, template_folder="../views", static_folder="../static", url_prefix="")

@root_controller.route("/", methods=["GET"])
def root():
    return redirect(url_for('home_controller.home'))
    