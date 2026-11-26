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
class Tricycle(Vehicle):
    def __init__(self, plate_number, capacity, barangay):
        super().__init__(plate_number, capacity)
        self.__barangay = barangay

    def get_barangay(self):
        return self.__barangay

    def set_barangay(self, barangay):
        self.__barangay = barangay

    def compute_fare(self, distance_km):
        base_fare = 10
        fare_per_km = 2
        return base_fare + (fare_per_km * distance_km)

    def describe(self):
        return f"Tricycle {self.get_plate_number()} with capacity {self.get_capacity()} is assigned to Barangay {self.__barangay}."
