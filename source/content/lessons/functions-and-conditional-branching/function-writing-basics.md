---
title: How to Write a Function
ordernum: 301
tldr: |

  ## Basic function
  
  ~~~py
  def say_hello():
      print("Hello") 
  ~~~

  ## Arguments

  ~~~py
  def say_hello_to(somebody):
      print("Hello", somebody)
  ~~~


  ## Default arguments
  
  ~~~py
  def say_bye_to(somebody, addon = 'nice seeing you'):
      print("Goodbye", somebody, addon)
  
  say_bye_to('Dan')                      # Goodbye Dan nice seeing you
  say_bye_to('Fran', 'and good night')   # Goodbye Fran and good night
  ~~~
  
  ### Using named arguments

  ~~~py
  say_bye_to(addon = 'man', somebody = 'Stan')  #  Goodbye Stan man
  ~~~

  
  ## The `return` keyword

  ~~~py
  def do_hello(person):
      return "Hello {0}".format(person)

  do_hello("dan").upper()    #  HELLO DAN
  ~~~
---


### Key point

Unlike all the interactive programming we've done, note that nothing is executed until the function is actually called.


## Basic function body

~~~py

~~~

## Function with an argument

~~~py
def say_hello_at(somebody):
    print("Hello", somebody)
~~~

## Function with a default argument

~~~py
def say_hellox(you='dan'):
    print("Hey", you)
~~~


## Invoking functions

~~~py
def say_bye(name = "Dan", ps = "hope to see you again"):
    print("Goodbye %s, %s." % (name, ps))

~~~


### Alternative invocations


~~~py
2 + 2

say_bye('Tom')
say_bye('Mary', 'see you later')
say_bye(name = 'Tom')
say_bye(ps = 'toodles')
say_bye(name = 'Sean', ps = 'nice talking to you')
~~~


### Improper function calls



## Functions with return values


### The return keyword

~~~py
def make_hello():
    return "Hello"

x = make_hello()
print(x)
~~~


### ipython subtleties

~~~py
In [44]: make_hello()
Out[44]: 'Hello'

In [45]: say_hello()
Hello
~~~




~~~py
def make_bye(name = "Dan", ps = "hope to see you again"):
    return "Goodbye %s, %s." % (name, ps))
~~~



## Exercises

~~~py
def foo(a = 42, b = 20):
    return 20 * a
    
print(foo(100, 10))
# 2000
~~~

~~~py
def choo(a = "Fun", b = "Sun"):
    print(a, 'and', b)

x = choo(b = 'Run')
print(x)
~~~


~~~py
def stew(b = 42, a = 42):
    return "%s,%s" % (a, b)

def brew(a = 42, b = 99):
    return stew(a, b)

brew(30, 108)
# 108,30
~~~



## Checking code at runtime

~~~py
def dont_run_me_please():
    ITOLD_U_NOT_TO_RUN, ME, WHATS_WRONG_WITH_YOU

dont_run_me_please()
# name 'ITOLD_U_NOT_TO_RUN' is not defined
~~~


