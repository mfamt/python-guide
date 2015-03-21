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
h.pop('b')
~~~


## Alternatively: fail fast




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


## EAFP

[Easier to ask for forgiveness than permission](https://docs.python.org/3.4/glossary.html#term-eafp)

> This common Python coding style assumes the existence of valid keys or attributes and catches exceptions if the assumption proves false. This clean and fast style is characterized by the presence of many try and except statements. The technique contrasts with the LBYL style common to many other languages such as C.



## LBYL

[Look before you leap.](https://docs.python.org/3.4/glossary.html#term-lbyl)

>  This coding style explicitly tests for pre-conditions before making calls or lookups. This style contrasts with the EAFP approach and is characterized by the presence of many if statements.
>
> In a multi-threaded environment, the LBYL approach can risk introducing a race condition between “the looking” and “the leaping”. For example, the code, if key in mapping: return mapping[key] can fail if another thread removes key from mapping after the test, but before the lookup. This issue can be solved with locks or by using the EAFP approach.




## Exercises

~~~py
def test_s():
    pass
~~~



