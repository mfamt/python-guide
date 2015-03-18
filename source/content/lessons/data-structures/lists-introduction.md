---
title: Introduction to Lists and Mutable Data
ordernum: 605
references:
  - url: http://learnpythonthehardway.org/book/ex32.html
  - url: https://docs.python.org/3/tutorial/datastructures.html
  - url: https://developers.google.com/edu/python/lists
  - url: http://stackoverflow.com/questions/626759/whats-the-difference-between-list-and-tuples
tldr: |

  ~~~py
  ### Initializing a list
  a = ['Hawn, Goldie', 'Newman, Paul', 42]    
  ### Accessing an array's members
  print(a[0])
  # => Newman, Paul
  print(a[0:2][1])
  # => Newman, Paul

  ### Mutating a list
  a[1] = 'Kurt Russell'
  a[2] *= 2
  print(a[1:3])
  # => ['Kurt Russell', 84]

  ### Remove members of a list
  print(a.pop())
  # => 84
  print(a)
  # => ['Hawn, Goldie', 'Kurt Russell']
  del(a[0])
  print(a)
  # =>  ['Kurt Russell']
  a.pop()
  print(a)
  # => []

  ### Add to a list
  a.append("stuff")
  a.append("more stuff")
  print(a)
  # => ['stuff', 'more stuff']
  a.reverse()
  print(a[0])
  # => more stuff
  print(a.remove('stuff'))
  # => None
  print(a)
  # => ['more stuff']
  ~~~
---


A __list__ is a data structure that can hold many other objects. A list is denoted by the use of __square brackets__. 

Understanding the concept of lists will enable you to understand (and process) a wide variety of data formats.



### Initializing a list

Here's how to initialize a list containing two numbers:

~~~py
my_list = [42, -30.0]
~~~


### Accessing members of a list

Use square brackets to refer to an individual member of a list. The first technical detail to mind is that Python lists are __0-indexed__: the first element has an __index of 0__:

~~~py
my_list = [42, -30.0]
print(my_list[0])
# 42
print(my_list[1])
# -30.0
~~~


### Accessing a range in a list

~~~py
big_list = [10, 20, 30, 40, 50, 60]
print(big_list[2:4])
# [30, 40]
~~~



## The contents of a list


~~~py
x = ['a', 5, '42', 'z', 100, 300]
~~~



## Ranges

TK

~~~py

print(range(10))
# range(10)

print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
~~~


## Adding elements to a list

~~~py
a = ["cat", "dog", "bird"]
b = ["dog", "fish"]
c = b + a
print(c)
# ['dog', 'fish', 'cat', 'dog', 'bird']
~~~



## Removing elements to a list



### The `del` statement




