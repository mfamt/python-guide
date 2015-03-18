import os
from glob import glob
from time import sleep
import requests
from bs4 import BeautifulSoup

# Set up the paths and destinations
HTML_DIR = './data-hold/html'
PDF_DIR = './data-hold/pdfs'
GEOCODE_DIR = './data-hold/geocodes'
# Create the subdirectories
for d in [HTML_DIR, PDF_DIR, GEOCODE_DIR]:
    os.makedirs(d, exist_ok=True)

# Some constants
START_YEAR = 2003
END_YEAR = 2012
# Templates for URLs
BASE_DOMAIN = 'http://www.dallaspolice.net'
HTML_URL = BASE_DOMAIN + '/ois/ois{0}.html'
# Templates for saved files
HTML_FILE = os.path.join(HTML_DIR, '{0}.html')
# This is the table column format
HTML_INCIDENT_COLS = ('case_number', 'date', 'location', 'suspect_status',
    'suspect_weapon', 'suspects', 'officers', 'grand_jury_disposition')

PDF_FILE = os.path.join(PDF_DIR, '{0}.pdf')
GEOCODE_FILE = os.path.join(GEOCODE_DIR, '{0}.json')
