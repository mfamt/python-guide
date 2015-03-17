---
title: Building Webpage Templates with Jinja
ordernum: 2005
references:
  - url: http://jinja.pocoo.org/docs/
    title: Jinja Documentation
---


Jinja is a templating language that makes it easy to incorporate Python logic into the generation of text, most specifically, HTML for web applications.

~~~py
import time
tx = "Hello %s, the time is now %s"
print(tx % ('Dan', time.strftime("%H:%M")))
# => Hello Dan, the time is now 15:41
~~~

With Jinja:

~~~py
import time
import jinja2
tj = 'Hello {{ name }}, the time is now {{ timeobj.strftime("%H:%M") }}'
print(tj)
j = jinja2.Template(tj)
print(j.render(name = 'Dan', timeobj = time))
# => Hello Dan, the time is now 15:42
~~~


Note, for the most part, it's not a best practice to be passing the `time` module in an argument like this.


#### More logic:

~~~py
import jinja2
tj = "{% for n in names %} Hello {{ n.upper() }} {% endfor %}"

j = jinja2.Template(tj)
print(j.render(names = ['Jared', 'Gillian']))
# => Hello JARED  Hello GILLIAN 
~~~




## Hello Jinja

Example taken from Jinja's documentation on [Basic API Usage](http://jinja.pocoo.org/docs/dev/intro/#basic-api-usage)

~~~py
from jinja2 import Template
t = Template('Hello, {{ name }}!')
print(t.render(name = 'world'))   #  Hello, world!
# without a name:
print(t.render())                 #  Hello, !
~~~

## With logic

~~~py
t2 = Template('Hello, {{ name.upper() }}!')
print(t2.render(name = 'dan'))    # Hello, DAN!
~~~

## Executing blocks

~~~py
x
~~~
