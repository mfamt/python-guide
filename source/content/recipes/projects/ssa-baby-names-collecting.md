---
title: Collecting Baby Names from the Social Security Administration
ordernum: 1005
references:
  - url: http://www.ssa.gov/OACT/babynames/limits.html
depends_on:
  - download-and-unzip
---


### Collecting the data

~~~py
from os.path import basename, splitext
from os import makedirs
from io import BytesIO
from zipfile import ZipFile
import requests

SITEURL = 'http://www.ssa.gov/OACT/babynames/{0}'
babypaths = ('nationwide', 'names.zip'), ('state', 'state/namesbystate.zip')
for p, zipurl in babypaths:
    # Download the files    
    print("Downloading:", zipurl, 'Saving to: /%s' % p)
    zb = requests.get(SITEURL.format(zipurl)).content
    with ZipFile(BytesIO(zb)) as z:        
        makedirs(p, exist_ok = True)
        z.extractall(path = p, 
           members = [x for x in z.namelist() if 'txt' in x.lower()]) 
~~~






