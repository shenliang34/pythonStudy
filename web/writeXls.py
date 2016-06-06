
__author__ = 'Administrator'
from xlsxwriter.workbook import Workbook
# import win32api
import os

# Create an new Excel file and add a worksheet.
xlsname = "demo.xlsx"
workbook = Workbook(xlsname)
worksheet = workbook.add_worksheet("demo")

# Widen the first column to make the text clearer.
worksheet.set_column('A:F', 20)

# Add a bold format to highlight cell text.
bold = workbook.add_format({'bold': 1})

# Write some simple text.
worksheet.write('A1', 'Hello')

# Text with formatting.
worksheet.write('A2', 'gfag World', bold)

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

workbook.close()
# win32api.ShellExecute(0,"open",xlsname)
os.system(xlsname)