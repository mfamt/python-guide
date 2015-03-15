---
title: Tuples
order: 405
references:
  - url: https://docs.python.org/3/library/stdtypes.html#tuple
tldr: |

  ~~~py
  ### Initializing a tuple
  a = 'Hawn, Goldie', 'Newman, Paul', 42
  ### Accessing a tuple's members
  print(a[0])       #   Hawn, Goldie
  print(a[1])       #   Newman, Paul    
  print(a[-1])      #   42
  print(a[-2])      #   Newman, Paul
  
  ### Accessing slices of a tuple
  b = (1, 2, 3, 4, 5, 6)
  print(b[3:])     #   (4, 5, 6)
  print(b[3:5])    #   (4, 5)
  print(b[:4])     #   (1, 2, 3, 4)
  print(b[::2])    #   (1, 3, 5)
  print(b[3:5:2])  #   (4,)

  ### Concatenating tuples
  c = "8mm",
  d = 'Adaptation', 'Raising Arizona'
  e = c + d
  print(e)  #  ('8mm', 'Adaptation', 'Raising Arizona')

  ## Nested tuples
  f = ('Face/Off', ('The Rock', 'Con Air'))
  print(f[1])         #    ('The Rock', 'Con Air')
  print(c[-1][-1])    #    Con Air
  ~~~
---


Tuples are a sequence
