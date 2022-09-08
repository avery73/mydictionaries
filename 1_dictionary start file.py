import random

phonebook = {'Chris':'555−1111',
             'Katie':'555−2222',
             'Joanne':'555−3333'}



print()
print('*****  start section 1 - print dictionary ********')
print()

print(phonebook)
print(type(phonebook))

phone = phonebook['Chris']

print(phone)

print(len(phone))


mydictionary = dict(m=8, n=9)

print(mydictionary)

mydict = {}

print(mydict)


print()
print('*****  end section 1 ********')
print()





print()
print('*****  start section 2 - search dictionary ********')
print()

name = "Chris"

if name in phonebook:
    print(phonebook[name])
else:
    print(name, 'not found')





print()
print('*****  end section 2 ********')
print()







print()
print('*****  start section 3 - edit/append dictionary ********')
print()

print(phonebook)
phonebook['Chris'] = '555-0123'     # since he already exists, it will just update his 
phonebook['Joe'] = '555-4444'       # since he doesn't exist, it will add it
print(phonebook)



print()
print('*****  end section 3 ********')
print()






print()
print('*****  start section 4 - delete/remove from dictionary ********')
print()

#del phonebook['Chris']      # deletes from phonebook, will get KeyError if it doesn't exist
#print(phonebook)

print()
print('*****  end section 4 ********')
print()






print()
print('*****  start section 5 - iterate through keys, values, items ********')
print()

for key in phonebook:       # default in dictionary is to iterate through the keys, doesn't matter I typed key
    print(key)
    print(phonebook[key])   # prints values (phone numbers)

for value in phonebook.values():    # if you want values, need to say .values in order to cycle through
    print(value)


for k,v in phonebook.items():
    print('key:', k, '  value: ', v)

for tuple in phonebook.items():     # dict keys are immutable, values are mutable?!
    print(tuple)        # list is square bracket [], tuple is para ()


print()
print('*****  end section 5 ********')
print()





print()
print('*****  start section 6 - using get and clear ********')
print()


phone = phonebook.get("chris", "key not found")      # Chris is case sensitive
print(phone)

#phonebook.clear()       # clears phonebook
#print(phonebook)

print()
print('*****  end section 6 ********')
print()



print()
print('*****  start section 7 - using pop method ********')
print()


remove = phonebook.pop("Chris", "key not found")

print(remove)
print(phonebook)



print()
print('*****  end section 7 ********')
print()



print()
print('*****  start section 8 - using popitem ********')
print()


a = phonebook.popitem()     # picks random key and value but takes it out of dictionary, but always picks same thing
                            # it just picks the last element
print(a)
print(phonebook)



print()
print('*****  end section 8 ********')
print()


print()
print('*****  start section 9 - using random and converting to list ********')
print()

list_of_keys = list(phonebook)      # convert dict to list
print(list_of_keys)                 # if you comment everything else out, it should print 4 names (prints list of 4 keys)
random_key = random.choice(list_of_keys)    # gets actual random key
print(random_key)
print(phonebook[random_key])        # gets random key of dictionary, normally we do all this in one line

print(phonebook[random.choice(list(phonebook))])    # all of it in one line, does everything inside out


print()
print('*****  end section 9 ********')
print()