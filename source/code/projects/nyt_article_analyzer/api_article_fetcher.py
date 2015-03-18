#!/usr/bin/env

# # api_article_fetcher.py
# ## Part of the NYT Article Analyzer project
# ## Part of MFAMT: Python
# ## Written by: Dan Nguyen
# ## [https://twitter.com/dancow](https://twitter.com/dancow)
# ----

# ## Imports
# to resolve filenames in the system
import os
# to parse the json
import json
# to contact remote Web APIs
import requests
# To iterate between given dates
from datetime import date
from dateutil.rrule import rrule, DAILY


# ## Import API key from an external JSON file
# Assuming that your NYT API credentials are in a JSON
# file named, `~/.nyt_api_creds`
NYT_API_CREDFILE = os.path.expanduser("~/.nyt_api_creds")

# And assuming the contents looks like this:
#
#        {
#           "article_search_api_v2": "YOUR_NYTARTICLES_APIKEY"
#        }
with open(NYT_API_CREDFILE) as nyt_creds:
    creds = json.loads(nyt_creds.read())
    articles_api_key = creds['article_search_api_v2']



# ## Set up the API call
# Refer [to the NYT docs](http://developer.nytimes.com/docs/read/article_search_api_v2)
ARTICLES_API_ENDPOINT = "http://api.nytimes.com/svc/search/v2/articlesearch.json"
basic_params = {
    "api_key"    : articles_api_key,
    "fq"         : 'source.contains:("New York Times")',
    "begin_date" : None,
    "end_date"   : None,
    "page"       : None
}


# ## Parse the start and end dates
# Assuming these are the given values
day1 = str("20150101")
day2 = str("20150103")
date_1 = date(int(day1[0:4]), int(day1[4:6]), int(day1[6:8]))
date_2 = date(int(day2[0:4]), int(day2[4:6]), int(day2[6:8]))

# The NYT Article Search API expects begin_date and end_date
# to be in `YYYYMMDD` format:
days = [d.strftime("%Y%m%d") for d in
            rrule(DAILY, dtstart = date_1, until = date_2)]

# ## Iterate through each day

for day in days:
    pgnum = 0
    search_params = basic_params.copy()
    search_params.update({
        "begin_date" : day,
        "end_date"   : day,
        "page"       : pgnum
    })

    url = requests.Request(method = "GET",
        url = ARTICLES_API_ENDPOINT,
        params = search_params).prepare().url

    print(url)



## Todo: make a bunch of functions
# - get_api_key()
# - get_date_values()
# - fetch_nyt_articles_by_day(day = somedate, page = somepage, api_key = api_key)
