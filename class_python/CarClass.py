import datetime
# --- Define Car Class --- #
class Car:
  def __init__(self, brand, year, color, speed, transmission):
    self.brand  = brand
    self.year   = year 
    self.color  = color
    self.speed  = speed
    self.transmission = transmission

  def getSpeed(self):
    return f'Your max speed car is {self.speed} km/h'

  def getYear(self):
    ageOfCar   = datetime.datetime.now().year - self.year
    if ageOfCar == 1:
      return f'The age of car is {ageOfCar} year'
    return f'The age of car is {ageOfCar} years'

  def runningCar(self):
    pass

# Instance Object
LamborghiniVeneno = Car("Lamborghini", 2015, "green", 300, "automatic")
ToyotaSupra       = Car("Toyota", 2021, "white", 200, "manual")

# Testing Object
print(LamborghiniVeneno.getYear())
print(LamborghiniVeneno.getSpeed())

print(ToyotaSupra.getYear())
print(ToyotaSupra.runningCar())