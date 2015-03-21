---
title: File Input and Output
description: How to read and write to files
ordernum: 1100

references: 
  - url: https://docs.python.org/3/tutorial/inputoutput.html
  - url: https://docs.python.org/3/library/os.html#files-and-directories
introduction: |
  Read and writing to files is an important part of programming, as this is often the way that we will get data TK.

tldr: |
  
  ## Files and directories

  ### Making a nested directory
  
  ~~~py
  from os import makedirs
  makedirs("stairway/to/heaven", exist_ok = True)
  ~~~



---


### The `with` suite

~~~py
with open('filename.txt', 'r') as file:
    data = f.read()
~~~


### Making a directory

https://docs.python.org/3.4/library/os.html#os.makedirs
