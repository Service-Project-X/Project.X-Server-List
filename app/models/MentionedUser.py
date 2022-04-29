from sqlalchemy import Column, ForeignKey, INT, VARCHAR
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class MentionedUser(Base):
    __tablename__ = 'MentionedUser'
    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    schedule_id = Column(INT, ForeignKey("Schedule.id"))
    nickname = Column(VARCHAR(45), nullable=False)
    name = Column(VARCHAR(45), nullable=False)
    email = Column(VARCHAR(45), nullable=False)

    schedule = relationship("Schedule", back_populates="MentionedUser")
