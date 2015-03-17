---
title: String Concatenation and Formatting
ordernum: 265
tldr: |

  ~~~py
  a = "hello"
  b = "world"
  print(a + b)   # helloworld
  c = 42
  print(a + c)   # TypeError: Can't convert 'int' object to str implicitly
  print(a + str(c))  # hello42
  d = "100"
  print(c + int(d))  # 142

  ### String formatting
  d = "Hey %s"
  print(d)          #  Hey %s
  print(d % 'you')  #  Hey you
  print(d % 42)     #  Hey 42
  ~~~
---


