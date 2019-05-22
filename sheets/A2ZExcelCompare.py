import xlrd

excelOnePath = "sheet1.xlsx"
excelTwoPath = "sheet2.xlsx"

excelOne = xlrd.open_workbook(excelOnePath)
excelTwo = xlrd.open_workbook(excelTwoPath)

def headerCheck(excelOne,excelTwo):
    excelOneSheet = excelOne.sheet_by_index(0)
    excelTwoSheet = excelTwo.sheet_by_index(0)

    for col in range(excelOneSheet.ncols):
        #print(excelOneSheet.cell_value(0, col), excelTwoSheet.cell_value(0, col))
        if(excelOneSheet.cell_value(0,col) != excelTwoSheet.cell_value(0,col)):
            print("XXXX--- Crapped out ---XXXXX")
            print("header " + str(col))
            print(excelOneSheet.cell_value(0,col), excelTwoSheet.cell_value(0,col))
            return 0
    print("Both have same headers :)")


def topToBottomCheck(excelOne,excelTwo):
    headerCheck(excelOne, excelTwo)
    numberOfSheets = excelOne.nsheets
    for sheet in range(numberOfSheets):
        excelOneSheet = excelOne.sheet_by_index(sheet)
        excelTwoSheet = excelTwo.sheet_by_index(sheet)

        for row in range(excelOneSheet.nrows):
            for col in range(excelOneSheet.ncols):
                #print(excelOneSheet.cell_value(row, col), excelTwoSheet.cell_value(row, col))
                if(excelOneSheet.cell_value(row,col) != excelTwoSheet.cell_value(row,col) and col != 7):
                    print("\nXXXX--- Crapped out ---XXXXX\n")
                    print(excelOneSheet.cell_value(row,col), excelTwoSheet.cell_value(row,col))
                    print("Sheet : %s \nRow: %s \nColumn: %s" % (sheet+1,row+1, col+1))
                    return 0

    print("Both have same values throughout :)")




topToBottomCheck(excelOne,excelTwo)
