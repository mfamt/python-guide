import requests

def get_nyt_articles(api_key, begin_date, end_date, page = 0):
    """
    Make a basic call to the NYT articles API
    `begin_date` and `end_date` are in YYYYMMDD format
    returns a dict object
    """
    articles_endpoint = "http://api.nytimes.com/svc/search/v2/articlesearch.json"
    the_params = {
        "api-key"    : api_key,
        "fq"         : 'source.contains:("New York Times")',
        "begin_date" : begin_date,
        "end_date"   : end_date,
        "page"       : page
    }
    response = requests.get(articles_endpoint, params = the_params)

    return response.json()





