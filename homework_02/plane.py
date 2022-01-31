"""
создайте класс `Plane`, наследник `Vehicle`
"""
from base import Vehicle


class Plane(Vehicle):
    cargo: int
    max_cargo: int

