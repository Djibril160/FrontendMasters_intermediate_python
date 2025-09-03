class Car:
  runs = True

  def __init__(self, name):
    print("New car!")
    self.name = name

  def start(self, name):
    if self.runs:
      print(f"{name.capitalize()} car is started")
    else:
      print(f"{name.capitalize()} car is broken! :(")
    