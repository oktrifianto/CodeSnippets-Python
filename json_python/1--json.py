import json

x = '{ "name" : "John" , "age" : 30, "city" : "London"}'

# parse x variable
y = json.loads(x)

# result in a python dictionary
print(y)    # {'name': 'John', 'age': 30, 'city': 'London'}

# print value
print(y["age"])