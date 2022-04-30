from sqlalchemy import Column, ForeignKey, INT, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class FolderSchedule(Base):
    __tablename__ = 'FolderSchedule'
    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    folder_id = Column(INT, ForeignKey("Folder.id"))
    schedule_id = Column(INT, ForeignKey("ScheduleBase.id"))
    mainDivide_id = Column(INT, ForeignKey("MainDivide.id"))

    folder = relationship("Folder", back_populates="FolderSchedule")
    schedule = relationship("ScheduleBase", back_populates="FolderSchedule")
    mainDivide = relationship("MainDivide", back_populates="FolderSchedule")
