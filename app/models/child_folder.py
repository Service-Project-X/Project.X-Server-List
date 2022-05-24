from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, String
from sqlalchemy.orm import relationship
from app.db.mysql_conn import Base
from app.models.schedule import Schedule


class ChildFolder(Base):
    __tablename__ = 'child_folders'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    folder_id = Column(Integer, ForeignKey("folders.id"), nullable=True)
    child_folder_id = Column(Integer, ForeignKey("child_folders.id"), nullable=True)

    name = Column(String(45), nullable=False)

    folder = relationship("Folder", back_populates="child_folders")
    child_folder = relationship("ChildFolder", back_populates="child_folders")

    schedules = relationship("Schedule", back_populates="child_folder")
    child_folders = relationship("ChildFolder", remote_side="ChildFolder.id", back_populates="child_folder")
