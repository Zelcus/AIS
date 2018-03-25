import xlrd

workbook = xlrd.open_workbook("Spreadsheet.xlsx")

worksheet = workbook.sheet_by_index(0)

print("{0}".format(worksheet.cell(0,0).value))
