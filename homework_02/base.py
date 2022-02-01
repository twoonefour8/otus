from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    weight: int
    fuel: int
    fuel_consumption: int
    started: bool = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel <= 0:
                raise LowFuelError
            self.started = True

    def move(self, distance):
        diff = self.fuel - distance * self.fuel_consumption
        if diff < 0:
            raise NotEnoughFuel
        self.fuel = diff
