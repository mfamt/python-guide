


### Why

We want to know or do something:

*How many babies have been named Daniel in 2013?*

What we know involves gathering information in a pattern

*How many babies have been named Daniel in 2012 and 2013*

year_2012 = 12999
year_2013 = 1800

year_2012 + year_2013


### Simplify

- formulate the filename in your head
- open up a file.read()
- find "Daniel,M"
- look at the third column

the function is:

~~~py
def get_yob_filename(y):
    return "yob" + str(y) + ".txt"


def get_number_of_boys_named_daniel_for_yob(y):
    filename = get_yob_filename(y)
    text = open(filename).read()
    text.find

~~~



### Other babies

~~~py
def get_yob_filename(y):
    return "yob" + str(y) + ".txt"


def get_number_of_boys_or_fyob(y):
    filename = get_yob_filename(y)
    text = open(filename).read()
    text.find
~~~



*How many babies since 1890?*





*How man*





