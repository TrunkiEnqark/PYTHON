import json

json_object = {'7':9, '0':3, '8':4, '9':1}
# python_obj = json.loads(json_object)

print(json.dumps(json_object, sort_keys=True, indent=8))

# j_data = json.dumps(json_object)

# print(type(j_data))
# print(json_object["NAME"])

