from datetime import timedelta

class Config:
    """Set Flask config variables."""
    # import secrets; secrets.token_hex(16)
    SECRET_KEY = '58c53763d3e688497096a9dc14852f02'
    PERMANENT_SESSION_LIFETIME = timedelta(days=5)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///appname/sqlite.db'
    # STATIC_FOLDER = ''
    # TEMPLATES_FOLDER = ''

class ProdConfig(Config):
    # FLASK_ENV = 'production'
    # DEBUG = False
    # TESTING = False
    # SQLALCHEMY_DATABASE_URI = ''
    pass

class DevConfig(Config):
    # FLASK_ENV = 'development'
    DEBUG = True
    # TESTING = True
    pass
