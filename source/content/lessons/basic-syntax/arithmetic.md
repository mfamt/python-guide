---
title: Arithmetic in Python
ordernum: 210
references:
  - url: https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator
  - url: https://docs.python.org/3/library/functions.html
  - url: https://docs.python.org/3/library/functions.html#round

takeaway: |
  Those who are coming from different languages, or even Python 2.x, should be aware that __division__ always returns a `float`.

tldr: |

  ~~~py
  ### Basic arithmetic
  print(10 + 10)        # 20
  print(10 + 10.0)      # 20.0
  print(10 - 0.5)       # 9.5
  print(10 - -0.5)      # 10.5
  print(10 * 5)         # 50
  print(10 / 2)         # 5.0
  print(10 // 2)        # 5
  print(10 / 2 - 3)     # 2.0
  print(10 / (2 - 3))   # -10.0


  ### Less basic arithmetic
  print(10 % 4)         # 2
  print(10 ** 4)        # 10000

  ### Built-in math functions
  print(abs(-42))         # 42
  print(pow(2,6))         # 64
  print(round(4))         # 4
  print(round(4.237, 2))  # 4.24  
  ~~~

---



