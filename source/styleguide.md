

[Google](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html)
[Hitchhiker's Guide to Python](http://docs.python-guide.org/en/latest/writing/style/)
[Pep 8](https://www.python.org/dev/peps/pep-0008/)
[OpenStack](http://docs.openstack.org/developer/hacking/)

## General design

- Keep functions short
- But not too short
- Text as a general interface
- Don't change the data
- Command query
- Return text
- Be confident
- Avoid comments as much as possible

## Writing style



For now, it's best to keep this axiom in mind:

    You spend far more time reading code than you will writing code.



## Whitespace



### Indentation

- 4 spaces
- Disable tabs
- 

### Blank/empty lines

Within the body of a method, be sparing with empty lines, and try to not have more than one consecutive.

~~~py

if stuff_we_like == "hey":
  

    while true: 
        
        print("whats up")
~~~


~~~py

if stuff_we_like == "hey":
    while true:    
        print("whats up")
~~~


~~~py

def hello:
  print("hello")
def goodbye:
  print("goodbye")
~~~


#### No whitespace after a line

Configure sublime text properly


#### Whitespace around symbols

No whitespace immediately after or before the inside of parentheses, brackets, or spaces.

No white space before a comma or colon:

Use whitespace after every comma and colon

Use whitespace around every equals sign

Use whitespace around binary operators


### Booleans

`if x is False`
`if x is None`

Avoid double negatives

`if x is not None`


#### Comments

This only deals with the appearance of comments, not their actual content.


- Avoid inline comments unless they are brief
- IT's OK to have a space between comment and code








### Commands-per-line

### Line length

- Less than 80 characters - this was a constraint forced by technical limitations. But now, it's still good sense. More than 80 characters is usually a flag that a line is doing too much:

##### Separate URLs/filenames

~~~py
mydata = open("/project/data-source/documents/other-pages/2015/12/example.html", "r").read()
~~~


~~~py
myfile = "/project/data-source/documents/other-pages/2015/12/example.html"
mydata = open(myfile, "r").read()
~~~

##### Nested functions/control



~~~py
while true:
    if stuff == 'a':
        if hello == 'b':
            print("Hello world on this")
        
~~~



## Narrative design

### Variable names

Use underscores
For constants, use capital letters
Avoid numbers
The shorter the scope, the shorter the name
The longer the scope, the longer the name




## Comments

As [Google says](https://google-styleguide.googlecode.com/svn/trunk/pyguide.html#Comments): __Never describe code__

My writing teacher used to say: Show, don't tell.

Think of comments as footnotes or annotation



---------------



## Program design

### Variables

- No to Global variables
- Assign variables close to where they are used

### Conditional expressions

### Functions

#### Default argument values

### Generators

### Lambdas

### String formatting



### String compilation

Use a list to accumulate strings:

~~~py
my_big_string = []
my_big_string.append("Hello")
my_big_string.append("world,")
my_big_string.append("I'm")
my_big_string.append("fantastic.")
~~~

