#!/usr/bin/python3
"""Definition of City class."""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import State, Base
from sqlalchemy.orm import relationship


class City(Base):
    """City class that represents the 'cities' table."""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
