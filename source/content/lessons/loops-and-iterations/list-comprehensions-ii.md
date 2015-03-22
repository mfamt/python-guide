---
title: Unpacking Sequences
ordernum: 655
references:
  - url: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
tldr: |

  ## Variable assignments

  ~~~py
  a, b = 'Hello', 'world'
  print(a)                   # Hello
  print(b)                   # world
  ~~~

  ### Catchall 

  ~~~py
  a, *b = ('Hello', 'world', 'again')
  print(a)          # Hello
  print(b)          # ['world', 'again']
  ~~~



  ## Function arguments

  ~~~py
  names = ('Alice', 'Bob', 'Charles')
  "Hey {}, {}, {}, and {}".format(*names)  # 'Hey Alice, Bob, and Charles'
  ~~~
---


