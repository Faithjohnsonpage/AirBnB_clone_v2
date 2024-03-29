#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False,)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    cities = relationship("City", back_populates="places")
    user = relationship("User", back_populates="places")

    reviews = relationship("Review", back_populates="place",
        cascade="all, delete, delete-orphan")

    @property
    def reviews(self):
        """Returns the list of Review instances with place_id equals
        to the current Place.id"""
        list_reviews = []
        from models import storage
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                list_reviews.append(review)
        return list_reviews
