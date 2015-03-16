---
title: The Basics of Building a Web App With Flask
ordernum: 2010
references:
  - url: http://flask.pocoo.org/docs/0.10/quickstart/#quickstart
---



## Hello world

Taken directly from Flask's [Quickstart guide](http://flask.pocoo.org/docs/0.10/quickstart/#quickstart)

```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    app.run()
```


## Adding a new route

```py
@app.route('/easter/egg')
def egg_page():
    return 'You found the easter egg page!'
```

## Adding a variable route

```py
@app.route('/love/')
@app.route('/love/<name>')
def love_page(name = 'you'):
    return 'I love %s' % name
```


## Adding a 404

```py
@app.errorhandler(404)
def page_not_found(error):
    return "Wrong page"
```


## All together


```py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/easter/egg/')
def egg_page():
    return 'You found the easter egg page!'

@app.route('/love/')
@app.route('/love/<name>')
def love_page(name = 'you'):
    return 'I love %s' % name

@app.errorhandler(404)
def page_not_found(error):
    return "Wrong page. Error message: %s" % error


if __name__ == '__main__':
    app.run()
```
