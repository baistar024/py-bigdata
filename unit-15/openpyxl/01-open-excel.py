import openpyxl
# open a exists excel file
def showData(wb):
    #actiove(p) 选择活动工作表
    if wb == None:
        return
    ws = wb.active
    #读取行
    for row in ws.rows:
        print("")
        #读取每个单元格
        for cell in row:
            print(cell.value, end ="    ")

workbook = openpyxl.load_workbook("filtered.xlsx")
showData(workbook)
workbook.close()

workbook = openpyxl.load_workbook("../../data/example.xlsx", read_only = True)
showData(workbook)
workbook.close()

workbook = openpyxl.Workbook(write_only=True)
print(type(workbook))
#showData(workbook)
workbook.close()


def copySheet(wbs,wbd):
    if wbs == None:
        return
    ws = wbs.active
    wsd = wbd.active
    data =[]
    for row in ws.values:
        wsd.append(row)


workbook = openpyxl.load_workbook("../../data/example.xlsx")
wbd = openpyxl.Workbook()
wss = workbook.active
copySheet(workbook, wbd)
workbook.close()
wbd.save("copydata.xlsx")
wbd.close()

