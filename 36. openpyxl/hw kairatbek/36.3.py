from openpyxl import load_workbook
from openpyxl.styles import Font

excel = load_workbook('отчёт.xlsx')
page = excel["Sheet"]

ft = Font(bold=True)

page["F2"].font = ft
page["F2"] = "Итого"
leng = 3
while leng < 7:
    page[f"F{leng}"] = page[f"C{leng}"].value + page[f"D{leng}"].value + page[f"E{leng}"].value
    leng += 1

page["G2"].font = ft
page["G2"] = "Среднее"
leng = 3
while leng < 7:
    page[f"G{leng}"] = round((page[f"C{leng}"].value + page[f"D{leng}"].value + page[f"E{leng}"].value)/3, 2)
    leng += 1

i = 0
letter = ["C", "D", "E", "F", "G"]
page["B7"].font = ft
page["B7"] = "Итого"
while i < len(letter):
    page[f"{letter[i-3]}7"] = page[f"{letter[i-3]}3"].value + page[f"{letter[i-3]}4"].value + page[f"{letter[i-3]}5"].value + page[f"{letter[i-3]}6"].value
    i += 1

excel.save('отчёт.xlsx')