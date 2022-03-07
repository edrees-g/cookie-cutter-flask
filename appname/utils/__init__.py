import re
from functools import wraps
from flask import session, redirect, url_for

EMAIL_REGEX = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

######################################
#             DECORATORS             #
######################################
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user' not in session:
            # TODO: next=request.url, implement this to take them to
            # the initially requested endpoint
            return redirect(url_for('signin_controller.signin'))
        return func(*args, **kwargs)
    return wrapper

def logout_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'user' in session:
            return redirect(url_for('dashboard_controller.dashboard'))
        return func(*args, **kwargs)
    return wrapper

#######################################
#              FUNCTIONS              #
#######################################
def check_password(password):
    """
    The purpose of this function is to check if a
    password meets the minimum complexity requirements.

    Args:
        password (string): The password.
    
    Returns:
        string: 'PASS' or reason for failure
    
    Raises:
        None
    """
    # check the password minimum length requirement
    if len(password) < 8:
        return "Password does not meet the minimum length requirement."
    
    # check the password maximum length requirement
    if len(password) > 64:
        return "Password does not meet the maximum length requirement."
    
    # check the password for at least one digit
    if re.search(r"\d", password) is None:
        return "Password must contain at least one digit."
    
    # check the password for at least one upper case.
    if re.search(r"[A-Z]", password) is None:
        return "Password must contain at least one upper case letter."
    
    # check the password for at least one lower case.
    if re.search(r"[a-z]", password) is None:
        return "Password must contain at least one lower case letter."
    
    # check the password for at least one symbol.
    if re.search(r"[!@#$%^&*()]", password) is None:
        return "Password must contain at least one symbol."
    
    return "PASS"
