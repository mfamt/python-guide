---
title: Navigating the File System
description: How to find files and create directories
ordernum: 1111
  - url: https://docs.python.org/3/library/os.html#files-and-directories
tldr: |

  
  ## Getting filename stuff

  ~~~py
  import os.path
  p = "~/Downloads/example.txt"
  os.path.basename(p)    #  'example.txt'
  os.path.splitext(p)    #  ('~/Downloads/example', '.txt')
  os.path.dirname(p)     #  ('~/Downloads')
  os.path.expanduser(p)  #  '/Users/daniel/Downloads/example.txt' 
  ~~~


  ## File attributes

  ~~~py
  os.path.exists('/tmp')                   # True
  os.path.exists('~')                      # False
  os.path.exists(os.path.expanduser('~'))  # True
  t = '/tmp/somefile.txt'
  os.path.getsize(t)                       # 48894
  ~~~


  ## Globbing a directory

  ~~~py
  import glob
  glob.glob('/tmp/*')
                      #  ['/tmp/com.apple.launchd.5Hdjak3l2',
                      #   '/tmp/com.apple.launchd.abc39xale',
                      #   '/tmp/com.apple.launchd.rQjs93as']
  ~~~


  ## Constructing a path

  ~~~py
  os.path.join('/tmp', 'path', 'to', 'file.txt') # '/tmp/path/to/file.txt'
  ~~~

  ### Making a nested directory
  
  ~~~py
  from os import makedirs
  makedirs("stairway/to/heaven", exist_ok = True)
  ~~~
---
