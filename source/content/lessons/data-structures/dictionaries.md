---
title: Dictionaries
ordernum: 650
references:
  - url: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

tldr: |

  ## Accessing key-value pairs of a dictionary

  ~~~py
  d = {"name": 'apples', "quantity": 542 }
  d['name']           #   'apples'
  # Referencing a non-existent key throws an error
  d['foo']            #   KeyError: 'foo'
  ~~~

  ## Adding key-value pairs

  ~~~py
  # The ordering of elements is arbitrary and can change 
  # upon insertion
  d['price'] = 0.99   
  # d is now: {"name": 'apples', "price": 0.99 , "quantity": 542, }   

  # Only immutable types can be used as keys
  d[['my', 'list']] = 'oops'    # TypeError: unhashable type: 'list'
  ~~~



  ## Dictionary methods

  ~~~py
  k = {'name': 'Bob', 'age': 42}
  list(k.keys())    #  ['name', 'age']
  list(k.values())  #  ['Bob', 42]

  #  For non-existing keys-value pairs, 
  #   .get() returns None instead of throwing an error
  k.get('foo')        # None

  k.update({'name': 'Bobby', 'state': 'CA'})    
  # k is now: {'age': 42, 'name': 'Bobby', 'state': 'CA'}
  ~~~

  ## The `dict()` constructor

  ~~~py
  arr = [('sape', 42), ('guido', 88)]
  dict(arr)        #  #  {'sape': 42, 'guido': 88}
  ~~~

  ## Testing membership

  ~~~py
  zlist = {'a': 9, 'c': 'hello'}
  'a' in zlist          #  True
  42 in zlist           #  False
  42 in zlist.values()  # True
  ~~~

  ## Testing equality

  As with all mutable data structures, _equality_ is not the same as _identity_:

  ~~~py
  a = {'x': 1, 'y': 2}
  b = {'x': 1, 'y': 2}
  a == b                 # True
  a is b                 # False
  ~~~

  Dictionaries with the same key-value pairs, but in different _order_, will pass the equality test:

  ~~~py
  a = {'x': 1, 'z': [1, 2, 3], 'y': 2}
  b = {'y': 2, 'x': 1, 'z': [1, 2, 3]}
  a == b                                 # True
  ~~~
---



Stuff
