---
title: Count elements on NYTimes.com homepage
ordernum: 400
---


~~~py
import requests
resp = requests.get("http://www.nytimes.com")
resp.text.count("<img")
resp.text.count("<h2")
~~~
