# CS3 Pair Assessment: Fare System
# Authors: (Bern Ernest L. Lausa, Yoram Wainscot R. Castro)
# Section: (Cesium)
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Abstract base class for every public vehicle."""

    def __init__(self, plate_number, capacity):
        self.__plate_number = plate_number
        self.__capacity = capacity

    def get_plate_number(self):
        return self.__plate_number
    
    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        if type(capacity) == int and capacity > 0:
            self.__capacity = capacity
        else:
            print("Invalid capacity.")

@abstractmethod
def compute_fare(self, distance_km):
    pass
@abstractmethod
def describe(self):
    pass
  
# ===== Jeepney class (Developer A) ====
# ===== Jeepney class (Developer B) ====
