---
title: Tuples
ordernum: 405
references:
  - url: https://docs.python.org/3/library/stdtypes.html#tuple
tldr: |

  ~~~py
  ### Initializing a tuple
  a = 'Newman', 'Paul', 1925, 2008
  print(type(a))    # <class 'tuple'>
  ### Accessing a tuple's members
  print(a[0])       #   Newman
  print(a[1])       #   Paul
  print(a[-1])      #   2008
  print(a[-2])      #   1925
  
  ### Accessing slices of a tuple
  b = (1, 2, 3, 4, 5, 6)
  print(b[3:])     #   (4, 5, 6)
  print(b[3:5])    #   (4, 5)
  print(b[:4])     #   (1, 2, 3, 4)
  print(b[::2])    #   (1, 3, 5)
  print(b[3:5:2])  #   (4,)

  ### Concatenating tuples
  c =  'The Rock', 'Stanley' 
  d = 'Adaptation', 'Charlie'
  e = c + d   
  print(e)  #  ('The Rock', 'Stanley', 'Adaptation', 'Charlie')

  ## Nested tuples
  f = (c, d)
  print(f)          #  (('The Rock', 'Stanley'), ('Adaptation', 'Charlie'))
  print(f[1])       #  ('Adaptation', 'Charlie')
  print(f[-1][-1])  #   Charlie
  ~~~
---


Tuples are a sequence
