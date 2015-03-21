---
title: Working with Excel Files
references:
  - url: http://www.simplistix.co.uk/presentations/python-excel.pdf
  - url: https://secure.simplistix.co.uk/svn/xlrd/trunk/xlrd/doc/xlrd.html?p=4966
---


The [xlrd lib](https://github.com/python-excel/xlrd)

~~~sh
pip install xlrd
~~~


Working with a sheet

~~~py
from xlrd import open_workbook
with open_workbook('Workbook1.xlxs') as wb:
    for s in wb.sheets():
    print('Sheet:', s.name)
    for row in range(s.nrows):
        vals = [s.cell(row, col).value for col in range(s.ncols)]
        print ', '.join(vals)
~~~
