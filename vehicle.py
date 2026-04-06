
class Vehicle:
  def __init__(self, color, model, year):
    self.color = color
    self.model = model
    self.year = year

  def start(self):
    print("Vehicle starting")
  
  def stop(self):
    print("Vehicle stopping")

class Car(Vehicle):
  def __init__(self, color, model, year, doors, wheels):
    super().__init__(color, model, year)
    self.doors = doors
    self.wheels = wheels

car = Car("Grey", "Toyota", 2020, 4, 4)
print(car.color)
print(car.stop())
print(car.__dict__)

vehicles = [
  Vehicle("Red", "Honda", 2018),
  Car("Blue", "Ford", 2021, 4, 4)
]

for v in vehicles:
  if isinstance(v, Vehicle):
    print(f"Vehicle: {v.model}, Color: {v.color}, Year: {v.year}")
