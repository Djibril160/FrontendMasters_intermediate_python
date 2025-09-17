class Car:
  runs = True
  number_of_wheesl = 4
  accident_subits = 2

  def __init__(self, name):
    print("New car!")
    self.name = name

  def start(self, name):
    if self.runs:
      print(f"{name.capitalize()} car is started")
    else:
      print(f"{name.capitalize()} car is broken! :(")

  @classmethod
  def get_number_of_crashes(cls):
    return cls.accident_subits

    
c5 = Car("citro")
c5.start("citroo")
print(c5.accident_subits)

