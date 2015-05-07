import csv
import json
import os.path
import requests
import re
from os import makedirs
from xlrd import open_workbook
# URL: http://www.cde.ca.gov/ds/sd/sd/filessp.asp
XLS_DIR = "./data-hold/xls/coredata"
FINISHED_DIR = './data-hold/finished'
FRPM_SLUG = 'frpm--2014-2015'
FRPM_XLS_PATH = os.path.join(XLS_DIR, FRPM_SLUG + '.xls')
FRPM_URL = "http://www.cde.ca.gov/ds/sd/sd/documents/frpm1415.xls"
FRPM_HEADERS = {
    'academic_year': 0,
    'county_code': 1,
    'district_code': 2,
    'school_code': 3,
    'school_name': 6,
    'nslp_provision_status': 10,
    'free_meal_count': 18,
    'free_eligible_pct': 19,
    'frpm_count': 20,
    'frpm_eligible_pct': 21
}

makedirs(XLS_DIR, exist_ok = True)

# Download the file
resp = requests.get(FRPM_URL)
with open(FRPM_XLS_PATH, 'wb') as f:
    f.write(resp.content)

# Reopen the file because meh
book = open_workbook(FRPM_XLS_PATH)
# pick the sheet with the most rows
sheet = sorted(book.sheets(), key = lambda sheet: sheet.nrows, reverse = True)[0]
print(FRPM_XLS_PATH, "has", sheet.nrows, "rows")
## extract the data
data = []
for x in range(1, sheet.nrows - 1):
    cols = sheet.row_values(x)
    # first column should be 20xx-20xx
    if re.search('\d{4}-\d{4}', str(cols[0])):
        d = {}
        for h, idx in FRPM_HEADERS.items():
            d[h] = cols[idx]
        data.append(d)


print("There are", len(data), 'data rows all together')

# write a JSON
jname = os.path.join(FINISHED_DIR, 'frpm.json')
print("Writing to JSON:", jname)
with open(jname, "w") as jfile:
    jfile.write(json.dumps(data, indent = 2))

# write a CSV
cname = os.path.join(FINISHED_DIR, 'frpm.csv')
print("Writing to CSV:", cname)
writer = csv.DictWriter(open(cname, 'w', encoding = 'utf-8'),
   fieldnames = FRPM_HEADERS.keys(),
   delimiter=','
)
writer.writeheader()
for d in data:
    writer.writerow(d)
