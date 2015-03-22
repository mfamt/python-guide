---
title: String Functions
ordernum: 270
description: |
  String objects come with a variety of functions that can be used to transform strings tk.
references:
  - url: https://docs.python.org/3/library/string.html
  - url: https://docs.python.org/3/library/stdtypes.html#string-methods

tldr: |
  
  ~~~py
  'Hello world'.upper()           # HELLO WORLD
  'Hello world'.lower()           # hello world
  'Hello world'.title()           # Hello World

  ## Finding and replacing
  'She sells seashells'.count('he')   # 2
  'cat'.index('a')                    # 1
  'ello' in 'Hello world'             # True
  "Hello world".replace('world', 'you')  # Hello you

  "42fourtyTWO".isalnum()     # True
  '42_0'.isalnum()            # False

  ## Stripping and padding
  "  Hello world".strip()     # 'Hello world'
  "42".zfill(4)               # '0042'
  "Hello".ljust(7, 'X')       # 'HelloXX'
  "Hello".rjust(7, 'X')       # 'XXHello'
  ~~~

---




