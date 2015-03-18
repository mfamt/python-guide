---
title: String Indexing
ordernum: 266
references:
  - url: https://docs.python.org/3/tutorial/introduction.html#strings
tldr: |

  ~~~py
  s = "Paul Newman"
  print(s[0])         # P
  print(s[1])         # a
  print(s[6])         # e
  print(s[100])       # IndexError: string index out of range
  # Negative indices
  print(s[-1])        # n
  print(s[-2])        # a

  # String slices
  print(s[0:1])       # P
  print(s[0:2])       # Pa
  print(s[2:5])       # ul
  # Omitted slice parameters
  print(s[3:])        # l Newman
  print(s[:7])        # Paul Ne
  print(s[3:-2])      # l Newm
  ~~~
---


