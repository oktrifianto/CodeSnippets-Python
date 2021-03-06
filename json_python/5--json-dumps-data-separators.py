import json

data = {
  "name"  : "John",
  "age"   : 20,
  "married" : True,
  "divorced" : False,
  "pets"  : None,
  "cars" : [
    {
      "models" : "BMW i8", "year": 2020
    },
    {
      "models" : "Toyota Supra", "year" : 2019 
    }
  ]
}

print(json.dumps(data, indent=4, separators=(". ", " = ")))

# --- result --- #
"""
{
    "name" = "John". 
    "age" = 20. 
    "married" = true. 
    "divorced" = false. 
    "pets" = null. 
    "cars" = [
        {
            "models" = "BMW i8". 
            "year" = 2020
        }. 
        {
            "models" = "Toyota Supra". 
            "year" = 2019
        }
    ]
}
"""