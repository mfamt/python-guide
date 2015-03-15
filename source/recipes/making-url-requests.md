---
title: Making URL requests
references:
  - url: http://docs.python-requests.org/en/latest/
---


```py
import requests
resp = requests.get('http://www.example.com')
```


## Getting the result

```py
import requests
resp = requests.get('http://www.example.com')
stuff = resp.text
```


## Passing parameters

```py
payload = {'user': 'dan', 'date': '2015-01-01'}
resp = requests.get("http://www.example.com", params = payload)
print(resp.url)
```


