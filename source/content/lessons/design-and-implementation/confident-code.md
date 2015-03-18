---
title: Confident Code
ordernum: 8000
references:
  - url: https://practicingruby.com/articles/confident-ruby
---


## Assert early

~~~py
h = {'a': 2}
h.get('b')    # returns None
h['b']        # raises KeyError
~~~



## Secure the borders

~~~py
### reduce type checking, consolidate it in one place
~~~


~~~py
### Supply a default
x = None
y = x or 42
~~~



## Wrap stuff


~~~py
### wrap in iterable
def iterify(obj):
    if hasattr(obj, "__iter__"):          
        if not(isinstance(obj, str) or isinstance(obj, bytes)):
        # it is a non-string/byte iterable
            return obj
    elif obj is None:
    # return empty list
        return []

    # else, it's a string/bytes/or non-iterable
    return [obj]
~~~

~~~py
## Testing it
for thing in [None, 1, [1,2], "abc", b'stuff', {'a': 42}, range(1,2)]:
    print(iterify(thing))

# []
# [1]
# [1, 2]
# ['abc']
# [b'stuff']
# {'a': 42}
# range(1, 2)
~~~



