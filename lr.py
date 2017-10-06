import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import xlrd

DATA_FILE='DATA/fire_theft.xls'

# Step 1: read in data from the .xls file
# Ps: if you are  unfamilar with  xlrd, please read xlrd.py
book = xlrd.open_workbook(DATA_FILE, encoding_override='utf-8')
sheet = book.sheet_by_index(0)
print(sheet.row_values(1))
