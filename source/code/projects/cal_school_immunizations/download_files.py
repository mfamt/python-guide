# scrape
import re
import os.path
from urllib.request import urlopen
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from os import makedirs
XLS_DIR = "./data-hold/xls"
DOMAIN = "http://www.cdph.ca.gov"
INDEX_URL = urljoin(DOMAIN, '/programs/immunize/pages/immunizationlevels.aspx')
makedirs(XLS_DIR, exist_ok = True)

# Download the HTML listing
response = urlopen(INDEX_URL)
soup = BeautifulSoup(response.read())
all_urls = [a['href'] for a in soup.find_all('a') if a.attrs.get('href')]
for url in all_urls:
    # just get Kindergarten spreadsheet URLs
    if 'Kinder' in url and 'xls' in url:
        y1, y2 = re.search('(\d{2})-(?:\d{2})?(\d{2})', url).groups()
        ext = os.path.splitext(url)[1]
        # e.g. ./data-hold/xls/K--2005-2006.xls
        oname = os.path.join(XLS_DIR, "K--20{0}-20{1}{2}".format(y1, y2, ext))
        full_url = urljoin(DOMAIN, url)
        print("Downloading:\n {0}\n into: {1}".format(full_url, oname))
#       sample:
        # Downloading:
        #  http://www.cdph.ca.gov/programs/immunize/Documents/2007-2008%20CA%20Kindergarten%20Data.xls
        #  into: ./data-hold/xls/K--2007-2008.xls

        with urlopen(full_url) as xlsfile:
            with open(oname, 'wb') as ofile:
                ofile.write(xlsfile.read())
