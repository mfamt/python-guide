


~~~py
import requests
resp = requests.get("http://www.nytimes.com")
resp.text.count("<img")
resp.text.count("<h2")
~~~
