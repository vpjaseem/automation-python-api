import yaml
with open('2.2 yaml-sample.yml', "r") as file:
    data = yaml.safe_load(file)
print(data)
print(data['Abdul'])
print(data['Abdul']['Place'])

print(data['Anas'])
print(data['Anas']['Age'])
