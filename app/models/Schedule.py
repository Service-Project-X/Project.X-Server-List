from sqlalchemy import Column, INT, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Schedule(Base):
    __tablename__ = 'ScheduleBase'
    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    title = Column(VARCHAR(100), nullable=False)
    content = Column(VARCHAR(45), nullable=False)
    image = Column(VARCHAR(100), nullable=False)

    mentionedUsers = relationship("MentionedUser", back_populates="ScheduleBase")
    FolderSchedules = relationship("FolderSchedule", back_populates="ScheduleBase")
