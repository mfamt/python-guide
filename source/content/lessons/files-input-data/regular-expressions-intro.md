---
title: Introduction to Regular Expressions
ordernum: 1500
description: "A powerful tool for describing, and finding, patters in text."
references:
  - url: https://developers.google.com/edu/python/regular-expressions
  - url: https://docs.python.org/3/library/re.html
  - url: https://docs.python.org/3/howto/regex.html#regex-howto
tldr: |

  ## `re.search()`
  ~~~py
  import re
  pattern = '\d{1,3},\d{3}'
  sentence = 'He spent $42,081 last night.'
  re.search('zblah', sentence)   #  None
  ~~~
  
  ## Match object  
  ~~~py
  m = re.search(pattern, sentence)
  #  <_sre.SRE_Match object; span=(10, 16), match='42,081'>
  m.span()                       #  (10, 16)
  m.group()                      #  42,081 
  ~~~

  
  

---


## re.search

## Match objects

### Literal matching

## Basic regex
