import csv
import json
import os.path
import requests
import re
from os import makedirs
from xlrd import open_workbook

XLS_DIR = "./data-hold/xls/coredata"
FINISHED_DIR = './data-hold/finished'
# overall data
# http://www.cde.ca.gov/ds/dd/
# public school data
# http://www.cde.ca.gov/ds/si/ds/pubschls.asp
PUB_SCHOOLS_SLUG = 'public_schools'
PUB_SCHOOLS_PATH = os.path.join(XLS_DIR, PUB_SCHOOLS_SLUG + '.xls')
PUB_SCHOOLS_URL = "ftp://ftp.cde.ca.gov/demo/schlname/pubschls.xls"

# private school data
# http://www.cde.ca.gov/ds/si/ps/
PRIV_SCHOOLS_SLUG = 'private_schools--2014-2015'
PRIV_SCHOOLS_PATH = os.path.join(XLS_DIR, PRIV_SCHOOLS_SLUG + '.xls')
PRIV_SCHOOLS_URL = "http://www.cde.ca.gov/ds/si/ps/documents/privateschools1415.xls"


