person = {}         # person - name of dictionary, {} means its empty
person["fname"] = "Joe"     # key called "fname" and the value is "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"] # key is children, value is a list, to access values, use an index
person["pets"] = {"dog": "Fido", "cat": "Sox"} # dog and cat are keys

#print(person)
#print(type(person['children']))   # tells you it's a list
#print(person['children'][1])      # print individual element of list
#print(person['pets']['cat'])      # prints cat name

for entry in person['children']:
    print(entry)

for entry in person['pets']:
    print(person['pets'][entry])

# OR

#for entry in person['pets'].values():
#    print(entry)