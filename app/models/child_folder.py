from sqlalchemy import Column, ForeignKey, INT, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class ChildFolder(Base):
    __tablename__ = 'ChildFolder'
    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    folder_id = Column(INT, ForeignKey("Folder.id"), nullable=True)
    child_folder_id = Column(INT, ForeignKey("ChildFolder.id"), nullable=True)
    name = Column(VARCHAR, nullable=False)

    folder = relationship("Folder", back_populates="ChildFolder")
    child_folder = relationship("ChildFolder", back_populates="ChildFolder")

    schedules = relationship("Schedule", back_populates="MainDivide")
