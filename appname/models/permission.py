from appname.database import Base
from sqlalchemy import Column, Integer, String

class Permission(Base):
    __tablename__ = "Permissions"
    id = Column(Integer, primary_key=True)
    description = Column(String(32), unique=True, nullable=False)

    def __repr__(self):
        return "Permission ('{}', '{}')".format(self.id, self.description)
