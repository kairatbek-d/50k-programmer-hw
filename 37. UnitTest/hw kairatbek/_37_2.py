from openpyxl import Workbook

def excelFunc(*args, yacheika):
    try:
        sum = 0
        count = 0
        for x in args:
            if isinstance(x, int):
                sum+= x
                count+=1
        page[yacheika] = sum//count
        return page[yacheika].value
    except AttributeError as e:
        raise AttributeError(e)
    except IndexError as e:
        raise IndexError(e)

# created, filled
excel = Workbook()
page = excel.active
page["A3"] = "Bill"
page["B3"] = 44
page["C3"] = 32
page["D3"] = 56

# used in function
res = excelFunc(page["A3"].value, page["B3"].value, page["C3"].value, page["D3"].value, yacheika="E3")

# saved
excel.save('отчёт.xlsx')