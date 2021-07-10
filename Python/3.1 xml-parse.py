import xmltodict
with open('3.2 xml-sample.xml', "r") as file:
    data = xmltodict.parse(file.read())['root']
print(data)
print(data['Abdul'])
print(data['Abdul']['Age'])
print(data['Abdul']['Place'])

print(data['Anas'])
print(data['Anas']['Age'])
print(data['Anas']['Place'])
