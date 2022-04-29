from sqlalchemy import Column, INT, BLOB
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class MainDivide(Base):
    __tablename__ = 'MainDivide'
    id = Column(INT, nullable=False, autoincrement=True, primary_key=True)
    user_team_id = Column(INT, nullable=True)
    user_id = Column(INT, nullable=True)
    team_id = Column(INT, nullable=True)
    divider = Column(BLOB, nullable=False, default=False)
