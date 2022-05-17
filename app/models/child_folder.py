from sqlalchemy import Column, ForeignKey, INT, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class ChildFolder(Base):
    __tablename__ = 'ChildFolderBase'
    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    folder_id = Column(INT, ForeignKey("Folder.id"), nullable=True)
    child_folder_id = Column(INT, ForeignKey("ChildFolderBase.id"), nullable=True)
    name = Column(VARCHAR, nullable=False)

    folder = relationship("Folder", back_populates="ChildFolderBase")
    child_folder = relationship("ChildFolderBase", back_populates="ChildFolderBase")

    schedules = relationship("Schedule", back_populates="MainDivide")
