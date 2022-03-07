# Define Class
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age  = age

  # methods
  def sayHello(self):
    return "Hello {0}".format(self.name)

  def sayAge(self):
    return f"Your age is {self.age}"

# create objects 
a = Person("Amelia", 23)
b = Person("Deby", 28)

# --- print ---
print(a.name)         # Amelia
print(a.sayHello())   # Hello Amelia
print(a.sayAge())     # Your age is 23

print(b.sayHello())   # Hello Deby