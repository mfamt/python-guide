---
title: Sequence Operations
ordernum: 425
references:
  - url: https://docs.python.org/3/library/stdtypes.html#common-sequence-operations
tldr: |
  
  ~~~py
  a = range(0, 10)
  len(a)      #  10
  min(a)       #   0
  max(a)       #   9
  ~~~

  ## Membership tests and functions

  ~~~py
  b = 'Black Mamba', 'Cottonmouth', 'Copperhead', 'Cottonmouth'
  'Cottonmouth' in b  # True
  'Mamba' in b        # False
  'Copper' not in b   # True
  b.index('Cottonmouth')           # 1
  b.count('Cottonmouth')    # 2
  ~~~
---


## Methods that act on a sequence


## Methods belonging to a sequence

