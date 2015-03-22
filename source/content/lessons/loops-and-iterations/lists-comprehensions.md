---
title: List Comprehensions
ordernum: 650
references:
  - url: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
  - url: http://norvig.com/spell-correct.html

tldr: |
  
  ## Mapping values 

  ~~~py
  nums = [1, 2, 3]
  [x * 10 for x in nums]     #  [10, 20, 30]
  ~~~

  ## Filtering with `if`

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

~~~py
### Unpacking variables with tuples
a = ('Clinton', 'Bill'), ('Bush', 'George')
names = [" ".join((first_n, last_n)) for last_n, first_n in a]
print(names)    #   ['Bill Clinton', 'George Bush']
~~~


## Nested list comprehension


