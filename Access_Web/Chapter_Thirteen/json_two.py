import json

data = '''[
    {"id":"001",
    "x":"2",
    "name":"chuck"
    },
    {"id":"009",
    "x":"7",
    "name":"john"
    }
]'''
info = json.loads(data)

print("User count:", len(info))
for item in info:
    print("Name", item['name'])
    print("ID", item['id'])
    print("Attribute", item['x'])
