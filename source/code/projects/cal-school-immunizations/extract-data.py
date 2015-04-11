import re
import json
from glob import glob
from xlrd import open_workbook
XLS_DIR = "./data-hold/xls"
pre_2012_headers = ['school_code', 'county', 'school_type', 'district_code', 'school_name',
'enrollment', 'uptodate_num', 'uptodate_pct', 'conditional_num', 'conditional_pct',
'pme_num', 'pme_pct', 'pbe_num', 'pbe_pct', 'dtp_num', 'dtp_pct', 'polio_num',
'polio_pct', 'mmr1_num', 'mmr1_pct', 'mmr2_num', 'mmr2_pct', 'hepb_num', 'hepb_pct',
'vari_num', 'vari_pct']
post_2012_headers = ['school_code', 'county', 'school_type', 'district_name', 'city',
'school_name', 'enrollment', 'uptodate_num', 'uptodate_pct', 'conditional_num', 'conditional_pct',
'pme_num', 'pme_pct', 'pbe_num', 'pbe_pct', 'dtp_num', 'dtp_pct', 'polio_num',
'polio_pct', 'mmr_num', 'mmr_pct', 'hepb_num', 'hepb_pct', 'vari_num', 'vari_pct', 'reported']

data = []
for xlsname in glob(XLS_DIR + '/*.xls*'):
    # extract the year numbers from the file name
    # e.g. "2006" and "2007" from "K--2006-2007.xls"
    yr_1, yr_2 = re.search('(\d{4})-(\d{4})', xlsname).groups()
    year = int(yr_1)
    headers = pre_2012_headers if year < 2012 else post_2012_headers
    # open the Excel workbook
    book = open_workbook(xlsname)
    # open the first non-empty spreadsheet
    sheet = [s for s in book.sheets() if s.nrows > 0][0]
    for x in range(1, sheet.nrows - 1):
        row = sheet.row_values(x)
        if re.search('\d{7}', str(row[0])):
            d = dict(zip(headers, row))
            d['year'] = year
            print(x, year, d['school_name'])
            data.append(d)

with open("data-hold/k-immune.json", "w") as jfile:
    jfile.write(json.dumps(data, indent = 4))
