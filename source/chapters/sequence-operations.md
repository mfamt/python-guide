---
title: Sequence operations
ordernum: 425
references:
  - url: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
tldr: |
  
  ~~~py
  a = range(0, 10)
  print(len(a))
  # => 0
  print(min(a))
  # => 0
  print(max(a))
  # => 9
  b = 'Black Mamba', 'Cottonmouth', 'Copperhead', 'Cottonmouth'
  print('Cottonmouth' in b)
  # => True
  print('Mamba' in b)
  # => False
  print('Copper' not in b)
  # => true
  print(b.index('Cottonmouth'))
  # => 1
  print(b.count('Cottonmouth'))
  # => 2

  # Strings are sequences, too
  print("Cottonmouth".count('t'))
  # => 3
  print('mouth' in 'Cottonmouth')
  # => True
  ~~~
---


## Methods that act on a sequence


## Methods belonging to a sequence

