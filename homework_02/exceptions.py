"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(BaseException):
    pass


class NotEnoughFuel(Exception):
    def __str__(self):
        return 'Недостаточно топлива для преодоления дистанции'


class CargoOverload(Exception):
    def __str__(self):
        return 'Перегруз'
