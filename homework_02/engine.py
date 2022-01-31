from abc import ABC

"""
create dataclass `Engine`
"""


class Engine(ABC):
    def __init__(self, volume, pistons):
        self.volume = volume
        self.pistons = pistons
