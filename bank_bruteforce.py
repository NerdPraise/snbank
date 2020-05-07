import json


with open('customer.txt') as json_file:
    data = json.load(json_file)
    print(json_file.read())
    print(data)