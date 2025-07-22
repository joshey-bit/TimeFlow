from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import os

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///../db/timeflow.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP)
    logs = relationship("Log", back_populates="user")

class Activity(Base):
    __tablename__ = "activities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    logs = relationship("Log", back_populates="activity")

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    activity_id = Column(Integer, ForeignKey("activities.id"))
    timestamp_start = Column(TIMESTAMP, nullable=False)
    timestamp_end = Column(TIMESTAMP)
    category = Column(String)
    confidence_score = Column(Float)
    user = relationship("User", back_populates="logs")
    activity = relationship("Activity", back_populates="logs")
