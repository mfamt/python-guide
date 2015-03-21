---
title: Object Orientation
ordernum: 3200
---


~~~py
from datetime import date
class Person:
    def __init__(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.birthdate  = date(*[int(d) for d in birthdate.split('-')])

    def age():
        t, b = date.today(), self.birthdate
        return t.year - b.year - int((t.month, t.day) < (b.month, b.day))

    def full_name():
        "{0} {1}".format(self.first_name, self.last_name)
~~~


~~~py
from datetime import date
def create_person(first_name, last_name, birthdate):
    p = dict()
    p['first_name'] = first_name
    p['birthdate']  = date(*[int(d) for d in birthdate.split('-')])
    return p
  
def age(p):
    t, b = date.today(), p['birthdate']
    return t.year - b.year - int((t.month, t.day) < (b.month, b.day))



def full_name(p):
    "{0} {1}".format(p['first_name'], p['last_name'])

~~~

