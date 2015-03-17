---
title: Solving FizzBuzz and Euler Question 1
ordernum: 300
references:
  - url: http://c2.com/cgi/wiki?FizzBuzzTest
    title: Fizz Buzz Test
  - url: http://blog.codinghorror.com/why-cant-programmers-program/
    title: "Why Can't Programmers...Program?"
  - url: http://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/
    title: Using FizzBuzz to Find Developers who Grok Coding
---





### With a really verbose `for`-loop

~~~py
total = 0
for x in range(1000):
    if x % 3 == 0:
        total += x
    elif x % 5 == 0:
        total += x
    else:
        total += 0

print(total) 
~~~

### More compact logic

~~~py
total = 0
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        total += x
print(total)
~~~


### Using a function

~~~py
def foo(x):
    if x % 3 == 0 or x % 5 == 0:
        return x
    else:
        return 0

print(sum(foo(x) for x in range(1000)))
~~~


### Using a list comprehension and `sum`

~~~py
print(sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0))
~~~



### Using `lambda`, `filter`, and `sum`

~~~py
print(sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1000))))
~~~



## FizzBuzz

via Imran Ghory, [Using FizzBuzz to Find Developers who Grok Coding](http://imranontech.com/2007/01/24/using-fizzbuzz-to-find-developers-who-grok-coding/), January 24, 2007:

> Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.


Common mistake:

~~~py
for x in range(100):
    if x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    elif x % 15 == 0:
        print('FizzBuzz')
    else:
        print(x)
~~~


Remember how the control will flow; all numbers divisible by `15` are _also_ divisible by `3` and `5`. Thus, the `x % 15 == 0` needs to come first:

~~~py
for x in range(100):
    if x % 15 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)
~~~




Ghory continues:

> Most good programmers should be able to write out on paper a program which does this in a under a couple of minutes.
>
> Want to know something scary ? – the majority of comp sci graduates can’t. I’ve also seen self-proclaimed senior programmers take more than 10-15 minutes to write a solution.


[Alex North](http://c2.com/cgi/wiki?FizzBuzzTest):

> I think Fizz-Buzz is "hard" for some programmers because (#1) it doesn't fit into any of the patterns that were given to them in school assignments, and (#2) it isn't possible to directly and simply represent the necessary tests, without duplication, in just about any commonly-used modern programming language.
> 
> On #1, that it doesn't match the patterns they memorized from lectures and class assignments: I think this makes it a good discriminator, because I wish to hire candidates who can think for themselves -- not those who are limited to copying solutions from others.
