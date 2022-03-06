import json

print(json.dumps(32))           # 32
print(json.dumps(None))         # null
print(json.dumps(91.2))         # 91.2
print(json.dumps({"name" : "John", "year" : 2022}))     # {"name": "John", "year": 2022}

# --- boolean --- #
print(json.dumps(False))        # false
print(json.dumps(True))         # true

# --- list --- #
print(json.dumps(["coffee", "tea"]))      # ["coffee", "tea"]