from flask import Blueprint, send_from_directory

favicon_controller = Blueprint("favicon_controller", __name__, template_folder="../views", static_folder="../static", url_prefix="/favicon.ico")

@favicon_controller.route("/", methods=["GET"])
def favicon():
    return send_from_directory(directory='static', path='images/favicon-32x32.png')
