---
title: Loops
ordernum: 510
references:
  - url: https://docs.python.org/3/tutorial/controlflow.html#for-statements
  - url: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
  - url: https://wiki.python.org/moin/ForLoop
  - url: https://wiki.python.org/moin/WhileLoop
  - url: http://stackoverflow.com/questions/8420705/example-use-of-continue-statement-in-python

tldr: |

  ## `for`-loop
  ~~~py
  for x in ('a', 'b', 'c'):
      print(x)           

  #  a
  #  b
  #  c  
  ~~~

  ## `while`-loop
  ~~~py
  y = 0
  while y < 3:
      print(y)
      y += 1             

  # 0
  # 1
  # 2
  ~~~



  ## `break`
  ~~~py
  z = 1
  while z < 1000:
      print(z)
      break

  # 1
  ~~~



  ## Looping through dictionary key-value pairs with `items()`
  ~~~py
  d = {'b': 99, 'z': 2000}
  for k, v in d.items():
      print(k, v) 

  # b 99
  # z 2000
  ~~~




---


When it comes to the topic of programming, I believe that there are two types of people:

1. People who are programmers
2. People who don't understand for-loops

tldr:



## For loop




## While loop

~~~py
x = 0
while x < 3:
    print("x is now %s") % x
    x += 1

# x is now 0
# x is now 1
# x is now 2
~~~



## Breaking the control flow



## Exercises




While loop




Nested for-loop

~~~py
for x in [1, 2, 3]:
    for y in ['a', 'b', 'c']:
        print("%s-%s") % (x, y)
~~~

output:

~~~
1-a
1-b
1-c
2-a
2-b
2-c
3-a
3-b
3-c
~~~



Nested for-loop, string appending

~~~py
a = []
for x in ["1", "2", "3"]:
    a.append(x)
    for y in ['a', 'b', 'c']:
        a.append(y)

print(",".join(a))
~~~
