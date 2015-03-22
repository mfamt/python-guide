---
title: Arithmetic in Python
ordernum: 210
references:
  - url: https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator
  - url: https://docs.python.org/3/library/functions.html
  - url: https://docs.python.org/3/library/functions.html#round

tldr_summary: |
  Those who are coming from different languages, or even Python 2.x, should be aware that __division__ always returns a `float`.

tldr: |

  
  ## Adding integers

  ~~~py
  10 + 20      #  30  
  ~~~

  ## Floating-point numbers
  ~~~py
  10 + 20.0    # 30.0
  ~~~

  ## Division

  In Python 3.x, the result of a division is always a `float`:

  ~~~py
  0 / 1       # 0.0
  ~~~

  Use `//` to do floor division:

  ~~~py
  10 // 2     # 5
  ~~~

  ## Other operators and built-in functions

  ~~~py
  10 % 4           # 2
  10 ** 4          # 10000
  abs(-42)         # 42
  pow(2,6)         # 64
  round(4)         # 4
  round(4.237, 2)  # 4.24    
  ~~~

---





### Old TLDR

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
