---
title: A spell checker
references:
  - url: http://norvig.com/spell-correct.html
---


A bloated version of Peter Norvig's classic, "How to Write a Spelling Corrector". Norvig demonstrates how to do so in 21 lines of Python code. We're going to do the same but in 400 lines of code.


## The `words` function

```py
import re
def words(text): 
    return re.findall('[a-z]+', text.lower()) 
```

```py
import collections

```

## Rewriting the `edits1` function



### The `splits()` function

```py
def splits(word):
    return [(word[:i], word[i:]) for i in range(len(word) + 1)]

for x in splits('dog'):
    print(x)
# => ('', 'dog')
# => ('d', 'og')
# => ('do', 'g')
# => ('dog', '')
```


#### The use of `range()`

```py
# range(len(word) + 1)
# i.e.
print(range(len('teh') + 1))
# => range(0, 4)
```

#### The `for`-loop

```py
for i in range(len('teh') + 1):
    print(i)
# => 0
# => 1
# => 2
# => 3
```

#### Creating the tuples

```py
print(('teh'[:0], 'teh'[0:]))
# => ('', 'teh')
print(('teh'[:1], 'teh'[1:]))
# => ('t', 'eh')
print(('teh'[:2], 'teh'[2:]))
# => ('te', 'h')
print(('teh'[:3], 'teh'[3:]))
# => ('teh', '')
```

#### Rewriting `splits()` as a `for`-loop 

```py
def splits(word):
    arr = []
    for i in range(len(word) + 1):
        tup = (word[:i], word[i:])
        arr.append(tup)
    return arr
```



### The `deletes()` function

```py
def deletes(split_word):
    return [a + b[1:] for a, b in split_word if b]

print(deletes(splits("teh")))
# => ['eh', 'th', 'te']
```

#### The `for`-loop

```py
for a in splits('teh'):
    if a[1]:
        print("Do something with:", a)
    else:
        print("Ignore:", a)

# => Do something with: ('', 'teh')
# => Do something with: ('t', 'eh')
# => Do something with: ('te', 'h')
# => Ignore: ('teh', '')
```

#### The list concatenation

```py
a, b = ('', 'teh')
print(a + b[1:])
# => eh
a, b = ('t', 'eh')
print(a + b[1:])
# => th
a, b = ('te', 'h')
print(a + b[1:])
# => te
```


#### Rewriting `deletes()` without a list comprehension

```py
def deletes(split_word):
    arr = []
    for a, b in split_word:
        if b:
            s = a + b[1:]
            arr.append(s)
    return arr
```



### The `transposes()` function

```py
def transposes(split_word):
    return [a + b[1] + b[0] + b[2:] for a, b in split_word if len(b) > 1]

print(transposes(splits('teh')))
# => ['eth', 'the']
```



### The `replaces()` function

```py
def replaces(split_word):
    return [a + c + b[1:] for a, b in split_word for c in 
      string.ascii_lowercase if b]
#=> ['aeh',
#=>  'beh',
#=>  'ceh',
#=>  'deh',
#=>  'eeh',
#=>   ...
#=>  'tew',
#=>  'tex',
#=>  'tey',
#=>  'tez']      
```



### The `inserts()` function

```py
def inserts(split_word):
    return [a + c + b for a, b in split_word for c in string.ascii_lowercase]

print(splits('teh'))
# => ['ateh',
# => 'bteh',
# => 'cteh',
# => 'dteh',
# => ...
# => 'tehw',
# => 'tehx',
# => 'tehy',
# => 'tehz']
```





## Modularizing it

spell_check()
