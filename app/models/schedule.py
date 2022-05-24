from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relationship
from app.db.mysql_conn import Base
# 아래꺼 안하면 또 못찾았다고 에러남
from app.models.mentioned_user import MentionedUser


class Schedule(Base):
    __tablename__ = 'schedules'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    folder_id = Column(Integer, ForeignKey("folders.id"), nullable=True)
    child_folder_id = Column(Integer, ForeignKey("child_folders.id"), nullable=True)
    title = Column(String(45), nullable=False)
    content = Column(String(300), nullable=True)
    image = Column(String(300), nullable=True)

    folder = relationship("Folder", back_populates="schedules")
    child_folder = relationship("ChildFolder", back_populates="schedules")

    mentioned_users = relationship("MentionedUser", back_populates="schedule")
