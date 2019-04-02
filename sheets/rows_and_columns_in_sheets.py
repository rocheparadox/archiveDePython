import xlrd
import sys

if len(sys.argv) > 1:
    workbook_name = sys.argv[1]
else:
    workbook_name = 'empty_url.xlsx'

#count = 0
my_workbook = xlrd.open_workbook(workbook_name)
sheets = my_workbook.sheets()
for sheet in sheets:
    print(sheet.name, sheet.nrows, sheet.ncols)
    #count = count + sheet.nrows
    #print(count)