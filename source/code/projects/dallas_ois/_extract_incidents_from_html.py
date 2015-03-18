def extract_incidents():
    """ Convenience method to extract incident list
        from all downloaded Dallas OIS HTML pages

    Pre:
          - HTML_DIR contains several .html pages
          - Presumably, fetch_pages() has successfully executed
    Post: Nothing
    Returns: A list of all the list of dicts extracted from each
       HTML file, i.e. extract_incidents_from_each_html()


    """
    incidents = []
    for hfile in glob(os.path.join(HTML_DIR, '*.html')):
        for incident in extract_incidents_from_each_html(hfile):
            incidents.append(incident)

    return incidents


def extract_incidents_from_each_html(html_filename):
    """ Parse a single Dallas OIS HTML page into a list of dicts

    Pre:  Nothing
    Post: Nothing
    Returns: A list of dicts, each one containing
        incident data as text mapped to HTML_INCIDENT_COLS.
        Also, the 'pdf_url' key contains an absolute URL to
        the incident narrative

    Args:
          - html_filename: filename of a downloaded HTML page
                           from Dallas OIS
    """
    incidents = []
    rawhtml = open(html_filename).read().encode('iso_8859_1').decode('utf-8')
    soup = BeautifulSoup(rawhtml)
    # in the case of the 2013-2014 (i.e. the default OIS homepage)
    #  there are two tables, one for each year. All other archive
    #  pages have a single table
    for table in soup.find("table").find_all("table"):
    # the first tr is always the headers row, so we skip it
        for row in table.find_all("tr")[1:]:
            cols = row.find_all('td')
            txtcols = [c.text.strip() for c in cols]
            incident = dict(zip(HTML_INCIDENT_COLS, txtcols))
            incident["pdf_url"] = BASE_DOMAIN + row.find('a')['href']
            # append to the list
            incidents.append(incident)

    return incidents
