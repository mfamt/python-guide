---
title: "Immunization Levels in California Schools"
ordernum: 1525
description: Gathering data
---


~~~py
# scrape
from urllib.request import urlopen
from bs4 import BeautifulSoup
from os import makedirs
import os.path
XLS_DIR = "./data-hold/xls"
INDEX_URL = 'http://www.cdph.ca.gov/programs/immunize/pages/immunizationlevels.aspx'
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
        print("Downloading {0} into {1}".format(url, oname))
        with urlopen(url) as xlsfile:
            with open(oname, 'wb') as ofile:
                ofile.write(xlsfile.read())
~~~


