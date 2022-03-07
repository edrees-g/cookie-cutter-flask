from appname.database import Base
from appname.models.user import User
from sqlalchemy import Column, Integer, String, ForeignKey

class Example(Base):
    __tablename__ = "Examples"
    id = Column(Integer, primary_key=True)
    example = Column(String(120), nullable=True, default='example column')
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    