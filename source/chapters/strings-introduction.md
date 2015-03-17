---
title: Strings, an Introduction
ordernum: 260
tldr: |

  ~~~py
  ### Single- and double-quotes have the same effect
  print('hello')
  print("hello")
  ### Use backslashes to escape quotes-within-quotes
  print("She said, \"Whoa!\"")   # She said, "Whoa!"
  print('He\'s happy \\')        # He's happy \

  ### Triple-quotes to enclose blocks of text
  mystring = """hello
  world, "how" 
     are 
        you"""
  print(mystring)     # hello
                      # world, "how"
                      #    are
                      #       you

  # print() can take multiple arguments
  hey = 'chumbawamba'
  print("hey")        #   hey
  print("hey", hey)   #   hey chumbawumba
  ~~~
---




