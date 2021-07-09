import json
with open('C:\\Users\\abvp\\Desktop\\json-sample.json', "r") as file:
    data = json.load(file)
print(data)

print(data['Abdul'])
print(data['Abdul']['Place'])

print(data['Anas'])
print(data['Anas']['Age'])
