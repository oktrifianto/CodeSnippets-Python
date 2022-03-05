# --------------------------
# Convert Dictionary to JSON 
# --------------------------

import json 

person = {
  "name"  : "John",
  "age"   : 30,
  "city"  : "London"
}

# convert into json string, not object
y = json.dumps(person)

print(y)  # return JSON [string]

# -------- return --------
# {"name": "John", "age": 30, "city": "London"}