class Car:  # cannot Car_Something or 123Car
    def __init__(self, model, year, speed) -> None: # type hinting
        self.model = model
        # self.modelA = model
        # self. can be anything
        self.year = year
        self.speed = speed

    def speed_up(self, increase):
        self.speed += increase


mercedes_car = Car('Mercedes', '2025', 600)
print(mercedes_car.speed)
mercedes_car.speed_up(100)
print(mercedes_car.speed)