class Engine:
    def start(self):
        print("Engine started")

class Wheels:
    def rotate(self):
        print("Wheels rotating")

class Car:
    def __init__(self):
        self.engine = Engine()  # composition
        self.wheels = Wheels() # composition

    def drive(self):
        self.engine.start()
        self.wheels.rotate()
        print("Car is moving")

# Creating a Car object using composition
my_car = Car()
my_car.drive()