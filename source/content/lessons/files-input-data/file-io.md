---
title: File Input and Output
description: How to read and write to files
ordernum: 1110
references: 
  - url: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
tldr_text: |
  Read and writing to files is an important part of programming, as this is often the way that we will get data TK.

tldr: |
  
  ## Opening a file for reading
  
  ~~~py
  # The second argument is "r" by default
  infile = open("example.txt", "r")
  ~~~

  ## Reading data from an opened file
  ~~~py
  infile.read()  
  infile.readline()
  ~~~


  ## Opening a file for writing
  ~~~py
  outfile = open("example.txt", "w")
  ~~~

  ## Writing data to an open file

  ~~~py
  outfile.write("Hello")
  outfile.write(str(42))
  ~~~

  ## Closing a file
  
  ~~~py
  infile.close()
  ~~~



  ## Using `with`
  ~~~py
  with open("example.txt", "r") as infile:
      data = infile.read()      
  ~~~



---


### The `with` suite

~~~py
with open('filename.txt', 'r') as file:
    data = f.read()
~~~


### Making a directory

https://docs.python.org/3.4/library/os.html#os.makedirs
