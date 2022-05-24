from sqlalchemy import Column
from sqlalchemy.types import Integer, Boolean
from sqlalchemy.orm import relationship
from app.db.mysql_conn import Base
from app.models.child_folder import ChildFolder
from app.models.schedule import Schedule


class Folder(Base):
    __tablename__ = 'folders'
    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    user_team_id = Column(Integer, nullable=False)

    user_id = Column(Integer, nullable=False)
    team_id = Column(Integer, nullable=False)
    divider = Column(Boolean, nullable=False)

    child_folders = relationship("ChildFolder", back_populates="folder")
    schedules = relationship("Schedule", back_populates="folder")
