from openpyxl import load_workbook

excel = load_workbook('report.xlsx')

page = excel["Sheet"]

# print(page) # <Worksheet "Sheet">
# print(page["B3"].value)

page["A5"] = "Среднее"

s = page["B2"].value + page['B3'].value + page['B4'].value
medium = s / 3
page["B5"] = medium

excel.save('report.xlsx')