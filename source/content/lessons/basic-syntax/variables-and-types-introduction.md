---
title: "Variables and Object Types, An Introduction"
ordernum: 220
tldr_summary: |
  Variables do not need to be declared.
  Everything is an object
tldr: |

  ~~~py
  a = 5
  b = 6
  print(a + b)          #   11
  c = b + a       
  print(c)              #   11
  b += 42
  print(b)              #   48
  print(c)              #   11
  a = 1000
  print(c)              #   11
  print(a + b + c)      #   1059
  print(a + b + c + x)  #   NameError: name 'x' is not defined

  ### the type() function
  print(type(42))         # <class 'int'>
  print(type(b))          # <class 'int'>
  print(type(1 / 3))      # <class 'float'>
  print(type(print(b)))   # <class 'NoneType'>
  print(type(print))      # builtin_function_or_method
  ~~~
---  




