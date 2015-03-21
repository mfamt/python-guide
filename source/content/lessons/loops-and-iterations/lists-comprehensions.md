---
title: Introduction to List Comprehensions
ordernum: 650
references:
  - url: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
  - url: http://effbot.org/zone/python-list.htm

tldr: |
  
  ### Filtering a list of strings

  ~~~py
  fnames = ['a.txt', 'b.pdf', 'c.txt']
  [x for x in fnames if 'txt' in x]      #  ['a.txt', 'c.txt']
  ~~~
---



## Basic

~~~py
numbers = []
for x in range(3):
    numbers.append(x * 10)

# alternative
numbers = [x * 10 for x in range(3)]
~~~


## With if statement


~~~py
numbers = []
for x in range(4):
    if x >= 2:
        numbers.append(x * 10)


numbers = [x * 10 for x in range(4) if x >= 2]
~~~



## Nested-for-loop as a list comprehension

~~~py
numbers = []
for x in [5, 6, 7]:
    for y in [-10, -20]:
        numbers.append(x * y)
~~~


~~~py
numbers = [x * y for x in [5, 6, 7] for y in [-10, -20]]
~~~


## Nested list comprehension


