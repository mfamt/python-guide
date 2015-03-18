---
title: File Input and Output
description: How to read and write to files
ordernum: 1100
references: 
  - url: https://docs.python.org/3/tutorial/inputoutput.html
introduction: |
  Read and writing to files is an important part of programming, as this is often the way that we will get data TK.
---


### The `with` suite

~~~py
with open('filename.txt', 'r') as file:
    data = f.read()
~~~
