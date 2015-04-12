---
title: Working with Excel Files
references:
  - url: http://www.simplistix.co.uk/presentations/python-excel.pdf
  - url: https://secure.simplistix.co.uk/svn/xlrd/trunk/xlrd/doc/xlrd.html?p=4966
  - url: http://www.cde.ca.gov/ds/si/ds/pubschls.asp
    title: California Public Schools Database
  - url: http://www.cdph.ca.gov/programs/immunize/pages/immunizationlevels.aspx
    title: Immunization Levels in Child Care and Schools
---


The [xlrd lib](https://github.com/python-excel/xlrd)

~~~sh
pip install xlrd
~~~


Setup

~~~py
# or if you want to work with the full file
# http://stash.compjour.org/data/ca-schools/pubschls
from urllib.request import urlopen
PUBSCHOOLS_URL = 'http://stash.compjour.org/data/ca-schools/pubschls-excerpt.xls'
IMMUNIZATION_URL = 'http://stash.compjour.org/data/ca-schools/immunization-K--2013-2014.xls'
PUBSCHOOLS_FNAME = '/tmp/pubschls.xls'
IMMUNIZATION_FNAME = '/tmp/immunization-k.xls'

x = urlopen(PUBSCHOOLS_URL)
f = open(PUBSCHOOLS_FNAME, 'wb')
f.write(x.read())
f.close()

x = urlopen(IMMUNIZATION_URL)
f = open(IMMUNIZATION_FNAME, 'wb')
f.write(x.read())
f.close()  
~~~


Working with a sheet

~~~py
from xlrd import open_workbook
wb = open_workbook(PUBSCHOOLS_FNAME)
sheets = wb.sheets()
sheet = sheets[0]
print('Sheet:', sheet.name)
# Sheet: pubschls
print('Number of rows', sheet.nrows)
# Number of rows 1111
print('Number of columns', sheet.ncols)
# Number of columns 48
~~~


Working with a row and xlrd.sheet.Cell data types

~~~py
row = sheet.row(5)
print(type(row))
# <class 'list'>
cell = row[7]
print(type(cell))
# <class 'xlrd.sheet.Cell'>
print(cell)
# text:'699 Serramonte Boulevard'
print(cell.value)
# 699 Serramonte Boulevard
~~~

Print the first 3 columns of the first 5 rows:

~~~py
for i in range(0,5):
    row = sheet.row_values(i)
    vals = ','.join(row[0:3])
    print("Row %s:" % i, vals)
~~~

Output:

~~~
Row 0: CDSCode,NCESDist,NCESSchool
Row 1: 41104130000000,0691033,
Row 2: 41104130113258,0691033,12003
Row 3: 41104130113266,0691033,12025
Row 4: 41104130113282,0691033,11945
~~~


## Conversions

### Convert to CSV


~~~py
import csv
from xlrd import open_workbook
writer = csv.writer(open(PUBSCHOOLS_FNAME + '.csv', 'w'))
wb = open_workbook(PUBSCHOOLS_FNAME)
sheet = wb.sheets()[0]
for i in range(sheet.nrows):
    writer.writerow(sheet.row_values(i))
~~~

### Convert to JSON

~~~py
import json
from xlrd import open_workbook
arr = []
wb = open_workbook(PUBSCHOOLS_FNAME)
sheet = wb.sheets()[0]
headers = sheet.row_values(0)
# skip first row
for i in range(1, sheet.nrows):
    d = dict(zip(headers, sheet.row_values(i)))
    arr.append(d)

with open(PUBSCHOOLS_FNAME + '.json', 'w') as jfile:
    jfile.write(json.dumps(arr, indent = 2))
~~~


