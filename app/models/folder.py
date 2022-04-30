from sqlalchemy import Column, INT, VARCHAR, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Folder(Base):
    __tablename__ = 'Folder'
    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    mainDivide_id = Column(INT, ForeignKey("MainDivide.id"))
    name = Column(VARCHAR(45), nullable=False)

    mainDivide = relationship("MainDivide", back_populates="Folder")

    ChildFolders = relationship("ChildFolder", back_populates="Folder")
    Schedules = relationship("Schedule", back_populates="Folder")
