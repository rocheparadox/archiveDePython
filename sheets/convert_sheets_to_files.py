import xlrd
import xlwt
import os
import shutil
import time
import sys

if len(sys.argv) > 1:
    workbook_name = sys.argv[1]
else:
    workbook_name = 'empty_url.xlsx'

current_dir=os.getcwd()
result_dir = current_dir + "/result"
if(os.path.isdir(result_dir)):
    shutil.copytree(result_dir,result_dir+str(int(time.time())))
    shutil.rmtree(result_dir)
os.mkdir(result_dir)


my_workbook=xlrd.open_workbook(workbook_name)
sheets = my_workbook.sheets()

for sheet in sheets:
    print(sheet.name)
    new_workbook = xlwt.Workbook()
    new_worksheet = new_workbook.add_sheet(sheet.name)

    for row in range(0,sheet.nrows):
        for col in range(0,sheet.ncols):
            new_worksheet.write(row, col, sheet.cell_value(row,col))

    new_workbook.save(result_dir+"/"+sheet.name+'.xlsx')


