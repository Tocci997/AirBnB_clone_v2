#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from os import getenv
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete-orphan",
                          backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """gets a list of all related objects of the class"""
            cty = models.storage.all(City)
            listall = []
            for city in list(cty.values()):
                if city.state_id == self.id:
                    listall.append(city)
            return listall
