def add(x, y):
  return x + y

def substract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def division(x, y):
  if (y == 0):
    raise ValueError('Can not divided by 0')
  return x / y

## manual testing
# print(division(10, 2))
# print(division(2, 0))