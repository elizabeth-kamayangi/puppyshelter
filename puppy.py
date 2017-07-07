import os
import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Shelter(Base):
    __tablename__ = 'shelter'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    address = Column(String(60))
    city = Column(String(60))
    state = Column(String(60))
    zipcode = Column(Integer)
    website = Column(String(90))


class Puppy(Base):
    __tablename__ = 'puppy'
    id = Column(Integer, primary_key=True)
    name = Column(String(60), nullable=False)
    date_of_birth = Column(String(60))
    gender = Column(String(8))
    weight = Column(String(8))
    shelter_id = Column(Integer, ForeignKey('shelter.id'))
    shelter = relationship(Shelter)



engine = create_engine('sqlite:///puppies.db')
Base.metadata.create_all(engine)
