class Vehicle:
  
  def __init__(self, make, model, fuel="gas"):
    self.make = make
    self.model = model
    self.fuel = fuel

  def __str__(self):
    return f"I drive my {self.make} {self.model} that runs on {self.fuel} fuel during the week end to show off ;:"


class Car(Vehicle):

  number_wheels = 4


class Truck(Vehicle):

  number_wheels = 6
  def __init__(self, make, model, fuel="diesel"):
    super().__init__(make, model, fuel)

week_end_car = Car("Dodge", "Camaro SS", "feu")

# print(week_end_car)

week_end_car.number_wheels = 3

print("number of wheels For the Class ", Car.number_wheels)
print("number of wheels For the instance ", week_end_car.number_wheels)

my_truck = Truck("Ford", "F-350")

print(f"my {my_truck.make} {my_truck.model} runs on {my_truck.fuel} having {my_truck.number_wheels} wheels")

print(isinstance(my_truck, Truck))

print(issubclass(Car, Vehicle))