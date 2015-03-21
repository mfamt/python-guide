---
title: Variables and Constants
ordernum: 305
references:
  - url: https://docs.python.org/3.4/library/constants.html
tldr_summary: |
  There are not many constants in Python's default namespace; the three most common:

  - `True`
  - `False`
  - `None`

  There is no `const` keyword or anything else to strictly enforce a constant. The convention is to name variables _intended_ to be constants in all-caps.

  Assigning 

tldr: |

  ~~~py
  # Python doesn't let us enforce constant values
  A_CONSTANT = 10
  A_CONSTANT = 20
  print(A_CONSTANT)   #  20

  # The built-in constants cannot be assigned a value
  Truth = False
  True = False        #  SyntaxError: can't assign to keyword
  ~~~

---

hi
