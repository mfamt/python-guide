---
title: Ranges
order: 410
references:
  - url: https://docs.python.org/3/library/stdtypes.html#ranges
tldr: |

  ```py
    ### range() with 1 argument
    a = range(6)
    print(type(a))
    # => range
    print(a)
    # => range(0, 6)
    print(a[5])
    # => 5
    print(a[-2])
    # => 4
    print(tuple(a))
    # => (0, 1, 2, 3, 4, 5)

    ### range() with 2 arguments
    b = range(-3, 2)
    print(tuple(b))
    # => (-3, -2, -1, 0, 1)

    ### range() with 3 arguments
    c = range(10, 50, 10)
    print(c)
    # => range(10, 50, 10)
    print(c[0])
    # => 10
    print(tuple(c))
    # => (10, 20, 30, 40)
    d = c[1:3]
    print(d)
    # => range(20, 40, 10)
    print(tuple(d))
    # => (20, 30)
  ```
    
