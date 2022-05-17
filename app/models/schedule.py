from sqlalchemy import Column, ForeignKey, INT, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Schedule(Base):
    __tablename__ = 'ScheduleBase'
    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    folder_id = Column(INT, ForeignKey("Folder.id"), nullable=True)
    child_folder_id = Column(INT, ForeignKey("ChildFolderBase.id"), nullable=True)
    title = Column(VARCHAR(100), nullable=False)
    content = Column(VARCHAR(45), nullable=True)
    image = Column(VARCHAR(100), nullable=True)

    folder = relationship("Folder", back_populates="Schedule")
    child_folder = relationship("ChildFolderBase", back_populates="Schedule")

    mentionedUsers = relationship("MentionedUser", back_populates="Schedule")

