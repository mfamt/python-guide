---
title: More Debugging
ordernum: 3000
references:
  - url: http://swcarpentry.github.io/python-novice-inflammation/07-defensive.html
  - url: http://stackoverflow.com/questions/16867347/step-by-step-debugging-with-ipython
  - url: https://zapier.com/engineering/debugging-python-boss/

tldr: |
  
  ### Using ipdb

  Install ipdb with `pip install ipdb`

  ~~~py
  def confusing_foo(a):
      b = a + 100 / 42 + 9281 / -42
      # start debugger
      import ipdb; ipdb.set_trace() 
  ~~~
---


