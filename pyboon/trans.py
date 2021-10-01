import os
from  openpyxl import  Workbook ,load_workbook
from pyboon import x,f

def csv2xl(csvfile):
    wb = Workbook()
    ws = wb.active

    txt = f.read(csvfile)

    for line in txt.split("\n"):
        print(line)
        ws.append(line.split(","))


    wb.save(csvfile.replace(".txt",".xlsx"))

def xl2csv(xlfile):
    wb = load_workbook(xlfile)
    ws = wb[wb.sheetnames[0]]

    lines = []
    for row in  ws.iter_rows():
        values = [cell.value for cell in  row]
        if values[0]:
            lines.append(",".join(values))
    
    f.write(os.path.join(os.getcwd(), xlfile.replace(".xlsx",".txt")),"\n".join(lines))
