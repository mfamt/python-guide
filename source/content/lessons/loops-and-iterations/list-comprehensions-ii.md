---
title: List Comprehensions and Logic
ordernum: 655
references:
  - url: http://norvig.com/spell-correct.html
  - 
tldr: |
  
  ~~~python
  ### Unpacking variables with tuples
  a = ('Clinton', 'Bill'), ('Bush', 'George')
  names = [" ".join((first_n, last_n)) for last_n, first_n in a]
  print(names)    #   ['Bill Clinton', 'George Bush']
  ~~~

---


