import pytest
from faker import Faker

fake = Faker()

homework = pytest.importorskip("homework_02")
module_base = homework.base
module_car = homework.car
module_engine = homework.engine


class TestCar:

    def test_init(self):
        weight = fake.pyint()
        fuel = fake.pyint()
        fuel_consumption = fake.pyint()
        car = module_car.Car(weight, fuel, fuel_consumption)

        assert isinstance(car, module_base.Vehicle)
        assert car.weight == weight
        assert car.fuel == fuel
        assert car.fuel_consumption == fuel_consumption

    def test_set_engine(self):
        volume = fake.pyint(1, 10)
        pistons = fake.pyint(2, 12)
        engine = module_engine.Engine(volume=volume, pistons=pistons)
        car = module_car.Car(0, 0, 0)
        car.set_engine(engine)
        assert car.engine is engine
        assert car.engine.volume == volume
        assert car.engine.pistons == pistons
