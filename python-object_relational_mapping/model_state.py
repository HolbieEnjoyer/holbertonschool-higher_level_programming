#!/usr/bin/python3
"""
This script connects to a MySQL database
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    def __init__(self, id, name):
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, nullable=False)
        name = Column(String(128), nullable=False)
