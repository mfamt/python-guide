---
title: Loops
order: 510
references:
  - url: https://docs.python.org/3.4/tutorial/datastructures.html#list-comprehensions
  - url: http://effbot.org/zone/python-list.htm
  - url: https://wiki.python.org/moin/ForLoop
  - url: https://wiki.python.org/moin/WhileLoop
---


When it comes to the topic of programming, I believe that there are two types of people:

1. People who understand for-loops
2. People for whom programming is an impossible, meaningless magic

Alternatively:

Those who understand for-loops. And those who aren't programmers.


```py
for x in [1, 2, 3]:
    print(x)

# 1
# 2
# 3
```


## For loop




## While loop

```py
x = 0
while x < 3:
    print("x is now %s") % x
    x += 1

# x is now 0
# x is now 1
# x is now 2
```



## Breaking the control flow



## Exercises




While loop




Nested for-loop

```py
for x in [1, 2, 3]:
    for y in ['a', 'b', 'c']:
        print("%s-%s") % (x, y)

1-a
1-b
1-c
2-a
2-b
2-c
3-a
3-b
3-c
```



Nested for-loop, string appending

```py
a = []
for x in ["1", "2", "3"]:
    a.append(x)
    for y in ['a', 'b', 'c']:
        a.append(y)

print(",".join(a))
```
