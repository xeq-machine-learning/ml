# xlrd guide
# xlrd means xls read package

# STEP 1: install xlrd
# pip install xlrd

# STEP 2: user guide
import xlrd

# open an Excel file
data_file = 'DATA/fire_theft.xls'
data = xlrd.open_workbook(data_file,encoding_override='utf-8')

# get a sheet object
# 3 methods
sheet = data.sheets()[0] # by sheet index
sheet = data.sheet_by_index(0) # by sheet index
sheet = data.sheet_by_name('fire_theft') # by sheet name

# get the values of the whole row or column
num=0 # the num of row or col
val = sheet.row_values(num)
val = sheet.col_values(num)

# get the cell value
cell_val = sheet.cell(0,0).value
cell_val = sheet.row(0)[0].value
