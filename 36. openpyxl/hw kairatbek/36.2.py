from openpyxl import Workbook
from openpyxl.styles import Font

excel = Workbook()
page = excel.active

ft = Font(bold=True)

page["B2"].font = ft
page["B2"] = "Сотрудник"
page["B3"] = "Bill"
page["B4"] = "Steve"
page["B5"] = "Elon"
page["B6"] = "Mark"

page["C2"].font = ft
page["C2"] = "Янв"
page["C3"] = 44
page["C4"] = 10
page["C5"] = 0
page["C6"] = 78

page["D2"].font = ft
page["D2"] = "Фев"
page["D3"] = 32
page["D4"] = 95
page["D5"] = 150
page["D6"] = 67

page["E2"].font = ft
page["E2"] = "Март"
page["E3"] = 56
page["E4"] = 74
page["E5"] = 175
page["E6"] = 86

excel.save('отчёт.xlsx')