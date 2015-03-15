---
title: Tuples
order: 405
references:
  - url: https://docs.python.org/3/library/stdtypes.html#tuple
tldr: |

  ```py
    ### Initializing a tuple
    a = ('Hawn, Goldie', 'Newman, Paul', 42)
    
    ### Accessing an tuple's members
    print(a[0])
    #=> Hawn, Goldie
    print(a[1])
    #=> Newman, Paul
    print(a[-1])
    #=> 42
    print(a[-2])
    #=> Newman, Paul
    print(a[0:2])
    ### ['Hawn, Goldie', 'Newman, Paul']

    ## Concatenating tuples
    b = a + ('Nicolas Cage', '8mm')
    print(b)
    # => ('Hawn, Goldie', 'Newman, Paul', 42, 'Nicolas Cage', '8mm')
    
    ## Nested tuples
    c = ('Adaptation', 'Raising Arizona', ('The Rock', 'ConAir'))
    print(c[1])
    # => Raising Arizona
    print(c[-1][-1])
    # => ConAir
  ```
---


Tuples are a sequence
