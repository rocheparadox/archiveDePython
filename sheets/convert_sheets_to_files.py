import xlrd
import xlwt
import os

current_dir=os.getcwd()
result_dir = current_dir + "/result"
os.mkdir(result_dir)

workbook_name='empty_url.xlsx'
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


