from appname.database import Base
from appname.models.permission import Permission
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    # TODO: perhaps a name column? First and last? or username?
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(128), nullable=False)
    permission = Column(Integer, ForeignKey(Permission.id), default=1)

    def __repr__(self):
        return "User ('{}', '{}')".format(self.email, self.permission)
        