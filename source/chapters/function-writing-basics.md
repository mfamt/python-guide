---
title: The basics of writing a function
order: 350
---



## Basic function body

```py
def say_hello():
    print("Hello")
```

## Function with an argument

```py
def say_hello_at(somebody):
    print("Hello", somebody)
```

## Function with a default argument

```py
def say_hellox(you='dan'):
    print("Hey", you)
```


## Invoking functions

```py
def say_bye(name = "Dan", ps = "hope to see you again"):
    print("Goodbye %s, %s." % (name, ps))

```


### Alternative invocations


```py
2 + 2

say_bye('Tom')
say_bye('Mary', 'see you later')
say_bye(name = 'Tom')
say_bye(ps = 'toodles')
say_bye(name = 'Sean', ps = 'nice talking to you')
```


### Improper function calls



## Functions with return values


### The return keyword

```py
def make_hello():
    return "Hello"

x = make_hello()
print(x)
```


### ipython subtleties

```py
In [44]: make_hello()
Out[44]: 'Hello'

In [45]: say_hello()
Hello
```




```py
def make_bye(name = "Dan", ps = "hope to see you again"):
    return "Goodbye %s, %s." % (name, ps))
```



## Exercises

```py
def foo(a = 42, b = 20):
    return 20 * a
    
print(foo(100, 10))
# 2000
```

```py
def choo(a = "Fun", b = "Sun"):
    print(a, 'and', b)

x = choo(b = 'Run')
print(x)
```


```py
def stew(b = 42, a = 42):
    return "%s,%s" % (a, b)

def brew(a = 42, b = 99):
    return stew(a, b)

brew(30, 108)
# 108,30
```
