from sqlalchemy import Column, INT, BLOB
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Folder(Base):
    __tablename__ = 'Folder'
    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    user_team_id = Column(INT, nullable=False)

    user_id = Column(INT, nullable=False)
    team_id = Column(INT, nullable=False)
    divider = Column(BLOB, nullable=False)

    ChildFolders = relationship("ChildFolder", back_populates="Folder")
    Schedules = relationship("Schedule", back_populates="Folder")
