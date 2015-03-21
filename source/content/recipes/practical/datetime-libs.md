---
title: Working with Dates and Times
ordernum: 1800
references:
  - url: https://docs.python.org/3/library/datetime.html
  - url: https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    title: "strftime() and strptime() Behavior"
  - url: http://arrow.readthedocs.org/en/latest/
  - url: https://unix4lyfe.org/time/
    title: What every programmer should know about time
  - url: http://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
  - url: http://stackoverflow.com/a/9754466/160863
---

## Standard datetime

~~~py
import datetime

### convert year, month, day integer to datetime.date object
datetime.date(2015, 12, 3)

### convert arbitrary string
datetime.datetime.strptime('November 24, 1987, 2:30PM', '%B %d, %Y, %I:%M%p')
# => datetime.datetime(1987, 11, 24, 14, 30)
~~~


### birthdate

    def age():
        t, b = date.today(), self.birthdate
        return t.year - b.year - int((t.month, t.day) < (b.month, b.day))



## Using dateutil


### How to iterate through a list of days

~~~py
from datetime import date
from dateutil.rrule import rrule, DAILY

xd = date(2008, 2, 27)
yd = date(2008, 3, 2)

for d in rrule(DAILY, dtstart = xd, until = yd):
    print( d.strftime("%Y-%m-%d"))

# 2008-02-27
# 2008-02-28
# 2008-02-29
# 2008-03-01
# 2008-03-02

~~~

