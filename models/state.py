#!/usr/bin/python3
"""
    State Module for HBNB project
"""
import os
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import storage_type
from models import storage


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        name = ""

        @property
        def cities(self):
            """Return a list of cities in a state
            """
            cities_in_state = []

            for key, value in storage.all().items():
                if key.split('.')[0] == "City":
                    city = value
                    if self.id == city.state_id:
                        if city not in cities_in_state:
                            cities_in_state.append(city)
            return cities_in_state
