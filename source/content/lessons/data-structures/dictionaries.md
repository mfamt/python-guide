---
title: Dictionaries
ordernum: 650
references:
  - url: https://docs.python.org/3/tutorial/datastructures.html#dictionaries
---



tldr:

~~~py

d = {"name": 'apples', "quantity": 542 }

### .keys()
print(d.keys())    #  dict_keys(['quantity', 'name'])
### tk??? ordered?
print(d.values())  #  dict_values([542, 'apples'])


### .update()
d.update({'quantity': 128})
print(d)           # {'name': 'apples', 'quantity': 128}
d.update({"price": 1.25, "quantity": 87})
print(d)           # {'quantity': 87, 'price': 1.25, 'name': 'apples'}

### dict() constructor
print(dict([('sape', 42), ('guido', 88)]))  #  {'sape': 42, 'guido': 88}

