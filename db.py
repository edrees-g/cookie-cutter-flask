from appname.extensions import bcrypt
from appname.database import Base, engine, db_session
from appname.models.user import User
from appname.models.example import Example
from appname.models.permission import Permission

Base.metadata.create_all(bind=engine)

admin_permission = Permission(description='admin')

example_user = User(email="admin@example.com", password=bcrypt.generate_password_hash('Password1!').decode('utf-8'), permission=1)
example_entry = Example(example="TESTING", user_id=1)

db_session.add(admin_permission)
db_session.add(example_user)

db_session.commit()
