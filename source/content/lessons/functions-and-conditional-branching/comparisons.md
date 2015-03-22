---
title: Comparisons
ordernum: 320
references:
  url: https://docs.python.org/3/reference/expressions.html#not-in
tldr: |
  ## Comparisons

  ~~~py
  10 > 5       #  True
  10 < 5       #  False
  10 == 10     #  True
  10 >= 10     #  True
  10 != 10     #  False
  ~~~

  ## Identity tests

  ~~~py
  'A' == 'A'   # True
  'A' is 'A'   # True
  5 == 5.0     # True
  5 is 5.0     # False
  5 is not 5.0 # True
  5 != 5.0
  ~~~

  ## Membership tests

  ~~~py
  'e' in 'Hello'        # True
  'a' not in 'Hello'    # True
  ~~~


---






## Exercises


~~~py
def foo(a, b):
    a == b

def goo(a, b):
    (a == b) == True
~~~

