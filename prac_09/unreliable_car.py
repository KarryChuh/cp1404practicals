import random
from prac_09.car import Car

class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability factor."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car only if a random number is less than the reliability."""
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0