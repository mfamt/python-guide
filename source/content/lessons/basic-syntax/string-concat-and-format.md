---
title: String Concatenation and Formatting
ordernum: 265
tldr: |

  ## Concatenation
  ~~~py
  "hello" + "world"   # 'helloworld'
  "hello" + 42        # TypeError: Can't convert 'int' object to str implicitly
  "hello" + str(c)    # 'hello42'
  42 + int("100")     # 142
  ~~~


  ## Formatting
  
  ~~~py
  d = "Hey %s"
  d % 'you'         #  'Hey you'
  d % 42            #  'Hey 42'
  ~~~

  ### The `format()` function

  ~~~py
  "hey {} meet {}".format("dan", "fran")    #  'hey dan meet fran'
  ~~~

  ### Positional arguments
  ~~~py
  "hey {1} eat {0}".format("veggies", "stan")  # 'hey stan eat veggies'
  ~~~

  ### Keyword arguments
  ~~~py
  '{name} is {age}'.format(age = 42, name = 'Pat')  #  'Pat is 42'
  ~~~
---


