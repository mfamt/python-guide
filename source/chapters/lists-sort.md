---
title: Sorting Sequences
ordernum: 610
references:
  - url: https://wiki.python.org/moin/HowTo/Sorting
tldr: |

  ~~~py
  ### Using sorted(), which returns a list
  arr = [9, 42, 5]
  tup = (8, -50, 104)
  print(sorted(arr))
  # => [5, 9, 42]
  print(sorted(tup))
  # => [-50, 8, 104]

  ### in-place sort using sort()
  print(arr)
  # => [9, 42, 5]
  arr.sort()
  print(arr)
  # => [5, 9, 42]
  tup.sort()
  # => AttributeError: 'tuple' object has no attribute 'sort'

  ### Sorting by key
  a = ('Apple', 'aloe')
  print(sorted(a))
  # => ['Apple', 'aloe']
  print(sorted(a, key = str.lower))
  # => ['aloe', 'Apple']
  b = ['1100', '5', '42']
  b.sort()
  print(b)
  # => ['1100', '42', '5']
  b.sort(key = int)
  print(b)
  # => ['5', '42', '1100']
  ~~~
---









## Sorting lists

~~~py
x = ["cat", "dog", "bird"]
y = sorted(x)
print(x)
# ['bird', 'cat', 'dog']
~~~


### sorted(list) vs list.sort() 




## Exercises

~~~python
print(sorted([4,3, '4', 'c', '11']))
~~~


~~~bash
print "hey $you"
~~~
