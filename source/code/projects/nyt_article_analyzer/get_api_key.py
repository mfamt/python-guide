import os
import json

def get_api_key():
    """
    Import API key from an external JSON file
    """
    # Assuming that your NYT API credentials are in a JSON file
    # named, `~/.nyt_api_creds`
    cred_file = os.path.expanduser("~/.nyt_api_creds")
    # Assuming the contents of .nyt_api_creds is JSON like this:
    # {
    #    "article_search_api_v2": "YOUR_NYTARTICLES_APIKEY"
    # }
    with open(cred_file) as nyt_creds:
        creds = json.loads(nyt_creds.read())
        return creds['article_search_api_v2']
