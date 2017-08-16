import json
from sys import stdout

# START
data = '''{
    "name": "bugs",
    "age": 76
}'''
obj = json.loads(data)

json.dump(obj, stdout)

# END
print(obj)
