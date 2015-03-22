---
title: "If/Else Statements"
ordernum: 560
references:
  - url: https://docs.python.org/3.4/tutorial/controlflow.html#if-statements
  - url: https://docs.python.org/3.4/reference/compound_stmts.html#elif
  - url: http://learnpythonthehardway.org/book/ex29.html
  - url: http://learnpythonthehardway.org/book/ex30.html
tldr: |
  ## Single `if` statement

  ~~~py
  if x > y:
      print('x is bigger than y')
  ~~~

  ## The `elif` keyword

  ~~~py
  if x > y:
      print("x is bigger than y")
  elif x < y:
      print("x is smaller than y")
  ~~~

  ## The `else` keyword

  ~~~py
  if x > y:
      print("x is bigger than y")
  elif x < y:
      print("x is smaller than y")
  else:
      print("x and y are equal")
  ~~~

  ## Inline `if` and `else`

  ~~~py
  a = 42
  b = 100
  print("Woo") if a > b else print("Boo")   # Boo
  ~~~

---



~~~py
def dan_test(x):
    if 'dan' in x.lower() 
~~~






