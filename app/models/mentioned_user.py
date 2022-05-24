from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relationship
from app.db.mysql_conn import Base


class MentionedUser(Base):
    __tablename__ = 'mentioned_users'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    schedule_id = Column(Integer, ForeignKey("schedules.id"), nullable=False)
    name = Column(String(45), nullable=False)
    email = Column(String(45), nullable=False)

    schedule = relationship("Schedule", back_populates="mentioned_users")
