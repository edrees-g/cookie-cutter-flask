import math
from appname.database import db_session
from appname.models.example import Example
from appname.utils import login_required
from flask import Blueprint, redirect, session, render_template, request, url_for, flash, abort

example_controller = Blueprint("example_controller", __name__, template_folder="../../views/dashboard", static_folder="../../static", url_prefix="/dashboard/examples")

@example_controller.route("/", methods=["POST"])
@login_required
def create_example():
    example_dictionary = dict(request.form.copy())
    for key in example_dictionary:
        value = example_dictionary.get(key)

        if value.strip() == "":
            flash("Invalid entry!", "danger")
            return redirect(url_for("example_controller.examples"))
        
        example_dictionary[key] = value.strip()
    
    new_example = Example(user_id=session['user'], **example_dictionary)
    db_session.add(new_example)
    try:
        db_session.commit()
    except Exception as e:
        # TODO: flask logging
        print(e)
        flash("Oops something went wrong, please contact us for assistance!", "danger")
        return redirect(url_for("example_controller.examples"))
    
    flash("Successfully created example!", "success")
    return redirect(url_for("example_controller.examples"))

@example_controller.route("/", methods=["GET"])
@login_required
def examples():
    page = request.args.get('page', 1, type=int)
    rows = request.args.get('rows', 5, type=int)

    num_rows = db_session.query(Example).filter(Example.user_id == session['user']).count()
    if (rows < 1):
        abort(404)
    num_pages = math.ceil(num_rows / rows)
    if num_rows != 0:
        if (page < 1) or (page > num_pages):
            abort(404)
    
    columns = Example.__table__.columns.keys()
    invalid_columns = ["user_id", "_sa_instance_state"]
    columns = [column for column in columns if column not in invalid_columns]

    columns.append("Edit")
    columns = list(map(str.capitalize, columns))

    examples = db_session.query(Example).filter(Example.user_id == session['user']).limit(rows).offset((page - 1) * rows)
    examples = [vars(example) for example in examples]

    return render_template("example.html", columns=columns, examples=examples, pages=num_pages, page=page, rows=rows)

@example_controller.route("/update", methods=["POST"])
@login_required
def update_example():
    try:
        example_dictionary = dict(request.form.copy())
        for key in example_dictionary:
            value = example_dictionary.get(key)

            if value.strip() == "":
                flash("Invalid entry!", "danger")
                return redirect(url_for("example_controller.examples"))
            
            example_dictionary[key] = value.strip()

        example_id = example_dictionary.pop("example_id")
        example_to_update = db_session.query(Example).filter(Example.id == example_id).first()
        for key, value in example_dictionary.items():
            setattr(example_to_update, key, value)
        
        db_session.commit()
    except Exception as e:
        # TODO: flask logging
        print(e)
    
    flash("Successfully updated example!", "success")
    return redirect(url_for("example_controller.examples"))


@example_controller.route("/delete", methods=["POST"])
@login_required
def delete_example():
    try:
        example_id = request.form.get("example_id")
        db_session.query(Example).filter(Example.id == example_id).delete()
        db_session.commit()
    except Exception as e:
        # TODO: Flask logging
        print(e)
    
    flash("Successfully deleted example!", "success")
    return redirect(url_for('example_controller.examples'))
