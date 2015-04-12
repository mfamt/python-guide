from math import ceil
from time import sleep

def get_nyt_articles_on_day(day, api_key = None):
    """
    `d` looks like: YYYYMMDD
    returns a list of article dict objects
    """
    articles = []
    if api_key is None:
        api_key = get_api_key()
    # make the call to page 0
    first_resp = get_nyt_articles(api_key = api_key, begin_date = day,
        end_date = day, page = 0)
    # add the results to the articles list
    articles.extend(first_resp['response']['docs'])
    # find the number of total "hits"
    hits = first_resp['response']['meta']['hits']
    # divide by 10 to get the number of pages to scrape
    total_pages = ceil(hits / 10)
    print("Total pages:", total_pages)
    for p in range(1, total_pages):
        print("Downloading page: ", p)
        resp = get_nyt_articles(api_key = api_key, begin_date = day,
           end_date = day, page = p)
        articles.extend(resp['response']['docs'])
        sleep(0.1) # rate limit is 10 per second

    return articles
