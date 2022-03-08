import json

def load_json(filename):
    with open(filename) as file:
        jsn = json.load(file)
        file.close()
    return jsn

person = load_json("json_example.json")
print(json.dumps(person,indent=4))
