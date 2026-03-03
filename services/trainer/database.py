import uuid

from sqlalchemy import Column, Float, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "sqlite:///experiments.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class Experiment(Base):
    __tablename__ = "experiments"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    status = Column(String)
    config = Column(Text)
    accuracy = Column(Float, nullable=True)
    loss = Column(Float, nullable=True)


Base.metadata.create_all(bind=engine)

