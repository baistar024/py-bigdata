import openpyxl
import os, shutil

wb = openpyxl.load_workbook("temp2.xlsx")
wslist = wb.sheetnames
for ws in wslist:
    if ws.lower() == "sheet":
        wslist.remove(ws)
print(wslist)

curdir = os.getcwd()
for wsi in wslist:
    ws = wb[wsi]
    print(wsi)
    os.chdir(curdir)
    # os.chdir(srcpath)
    # os.mkdir('dsc')
    # os.chdir(curdir)
    # shutil.copy()
    # print(type(ws),ws)
    os.chdir(r"./images/{}".format(wsi))
    i=1
    for row in ws.rows:
        if i == 1:
            i += 1
            continue
        print(row[0].value,row[2].value)
        # cmd =r'cp {} ./{}'.format(row[0].value ,'dsc')
        shutil.copy(row[0].value, r'./dsc/')
        i += 1

