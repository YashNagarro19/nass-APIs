import datetime
from sqlalchemy import String, Integer, Column, Text, Enum, DateTime
from database.database import Base

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True)
    fullname=Column(String(255),nullable=True)
    email=Column(Text,nullable=False,unique=True)
    password=Column(String(255),nullable=False)
    datetime=Column(DateTime, default=datetime.datetime.now(), nullable=False)
    description=Column(String(255),nullable=True)
    domain=Column(String(255),nullable=True)
    companySize=Column(Integer,nullable=True)
    