---
title: Web Requests with the Requests Library
ordernum: 1400
references:
  - url: http://docs.python-requests.org/en/latest/
  - url: https://docs.python.org/3/howto/urllib2.html


---





~~~py
import requests
resp = requests.get('http://www.example.com')
~~~


## Getting the result

~~~py
import requests
resp = requests.get('http://www.example.com')
stuff = resp.text
~~~


## Passing parameters

~~~py
payload = {'user': 'dan', 'date': '2015-01-01'}
resp = requests.get("http://www.example.com", params = payload)
print(resp.url)
~~~


