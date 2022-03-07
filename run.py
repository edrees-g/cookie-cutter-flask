from appname.main import create_app
from appname.database import db_session

app = create_app()

#######################################
#                FLASK                #
#######################################
@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

# @app.before_request
# def before_request_func():
#     pass

if __name__ == "__main__":
    app.run() # debug=True