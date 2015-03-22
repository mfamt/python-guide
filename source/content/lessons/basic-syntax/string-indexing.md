---
title: String Indexing
ordernum: 266
references:
  - url: https://docs.python.org/3/tutorial/introduction.html#strings
tldr: |

  ~~~py
  s = "Paul Newman"
  s[0]         # P
  s[1]         # a
  s[6]         # e
  s[100]       # IndexError: string index out of range
  # Negative indices
  s[-1]        # n
  s[-2]        # a

  # String slices
  s[0:1]       # P
  s[0:2]       # Pa
  s[2:5]       # ul
  # Omitted slice parameters
  s[3:]        # l Newman
  s[:7]        # Paul Ne
  s[3:-2]      # l Newm
  ~~~
---


