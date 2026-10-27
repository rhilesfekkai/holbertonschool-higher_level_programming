#!/usr/bin/python3
"""Define the City model."""

from sqlalchemy import Column, ForeignKey, Integer, String
from model_state import Base


class City(Base):
    """Represent a city in the cities table."""

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
