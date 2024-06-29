#!/usr/bin/python3
"""Defines a class <Review>."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """A class <Review> that inherits from <BaseModel>.

    Public class attributes:
        place_id (str): ...
        user_id (str): ...
        text (str): ...
    """
    __tablename__ = "reviews"
    text = Column(String(1024), nullable=False)
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
