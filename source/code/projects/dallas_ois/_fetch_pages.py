def fetch_pages():
    """ Download all of the webpages for Dallas OIS

    Pre:
          - Setup of data directories and constants
            has been completed.

    Post:
          - PDF_DIR contains a .html file for every OIS page,
              saved as the year of the original URL
              e.g. http://www.dallaspolice.net/ois/ois_2003.html
              is saved as: HTML_DIR/2003.html

    Returns: Nothing
    """
    # Manually get 2013-2014, which are both on one page
    url = HTML_URL.format("")
    dest_file = HTML_FILE.format('2013-2014')
    resp = requests.get(url)
    with open(dest_file, 'w') as f:
        f.write(resp.text)
        print("Saved {0} to {1}".format(url, dest_file))

    # Now get the rest of them
    for yr in range(START_YEAR, (END_YEAR + 1)):
        url = HTML_URL.format('_' + str(yr))
        resp = requests.get(url)
        ## save to disk
        dest_file = HTML_FILE.format(yr)
        with open(dest_file, 'w') as f:
            f.write(resp.text)
            print("Saved %s to %s" % (url, dest_file))

