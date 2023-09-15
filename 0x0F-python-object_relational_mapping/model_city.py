#!/usr/bin/python3
"""Definition of a City Model"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import State, Base


class City(Base):
    """City class that represents the cities table"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
