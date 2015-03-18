---
title: Mutable data
ordernum: 606
description: The implications of mutable data.
references:
  - url: https://docs.python.org/3.4/library/copy.html

tldr: |

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
  r[2][2] = 'Pie'
  deep_r[2][2] = 'The Dress'
  print(r[2])              # ['Yes', 2, 'Pie']
  print(shallow_r[2])      # ['Yes', 2, 'Pie']
  print(deep_r[2])         # ['Yes', 2, 'The Dress']
  ~~~

---




## Using the `copy` module


### Shallow copy

### deep copy
