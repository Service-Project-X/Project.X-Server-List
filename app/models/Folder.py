from sqlalchemy import Column, INT, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Folder(Base):
    __tablename__ = 'Folder'
    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    name = Column(VARCHAR(45), nullable=False)

    folderSchedules = relationship("FolderSchedule", back_populates="Folder")
