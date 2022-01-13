from openpyxl import Workbook

# first approach
# excel = Workbook()
# excel.save('./36. openpyxl/report.xlsx')


# second approach
excel = Workbook()
page = excel.active
page["A3"] = "Hello"
page["B3"] = 59
excel.save('testing.xlsx')