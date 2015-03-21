---
title: Mutable data
ordernum: 606
description: The implications of mutable data.
references:
  - url: https://docs.python.org/3.4/library/copy.html

tldr: |

  ## Shallow copying

  ~~~py
  import copy
  r = ["hello", ('Newman', 'Paul'), [1, 2, 3], 42]
  shallow_r = copy.copy(r)
  ~~~

  Changing the contents of a `list` won't affect its copy (i.e. `shallow_r`)

  ~~~py
  # Assignment does not make a new copy
  rx = r   # ["hello", ('Newman', 'Paul'), [1, 2, 3], 42]
  r[0] = 'bye'
  rx[0]                    #   'bye'
  shallow_r[0]             #   'hello'
  ~~~

  Similarly, altering the list, such as using its `pop()` method, won't affect its copy:
  
  ~~~py
  ### removing an item
  r.pop()
  len(r)            # 3
  len(rx)           # 4
  len(shallow_r)    # 4
  ~~~

  ## Changing a mutable member

  However, when doing a _shallow_ copy of a data structure, its _mutable_ members are _not_ copied. 

  ~~~py
  ### changing a mutable item
  r[2][0] = 'Yes'
  shallow_r[2][2] = "No"

  r[2]              #    ['Yes', 2, "No"]
  shallow_r[2]      #    ['Yes', 2, "No"]
  ~~~


  ~~~py
  ### deep copy
  deep_r = copy.deepcopy(r)
  r[2][2] = 'Pie'          # =>  r[2][2]
  deep_r[2][2] = 'The Dress'
  print(r[2])              # ['Yes', 2, 'Pie']
  print(shallow_r[2])      # ['Yes', 2, 'Pie']
  print(deep_r[2])         # ['Yes', 2, 'The Dress']
  ~~~

  ### Strings are not mutable

  ~~~py
  a = 'Hello'
  a.lower()      #   'hello'
  a             #   'Hello'
  ~~~

---




## Using the `copy` module


### Shallow copy

### deep copy


Old tldr:


  ~~~py
  import copy
  r = ["hello", ('Newman', 'Paul'), [1, 2, 3], 42]
  ### shallow copy
  shallow_r = copy.copy(r)
  r[0] = 'bye'
  print(r[0])              # bye
  print(shallow_r[0])      # hello
  ### removing an item
  r.pop()
  print(len(r))            # 3
  print(len(shallow_r))    # 4
  ### changing a mutable item
  r[2][2] = 300
  shallow_r[2][0] = "Yes"
  print(r[2])              # [1, 2, 300]
  print(shallow_r[2])      # [1, 2, 300]


  ### deep copy
  deep_r = copy.deepcopy(r)
  r[2][2] = 'Pie'          # =>  r[2][2]
  deep_r[2][2] = 'The Dress'
  print(r[2])              # ['Yes', 2, 'Pie']
  print(shallow_r[2])      # ['Yes', 2, 'Pie']
  print(deep_r[2])         # ['Yes', 2, 'The Dress']
  ~~~

  ### Strings are not mutable

  ~~~py
  a = 'Hello'
  a.lower()      #   'hello'
  a             #   'Hello'
  ~~~
