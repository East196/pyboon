import os,json
from  openpyxl import  Workbook ,load_workbook
from pyboon import x,f
from rich.console import Console

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

def to_json(d):
    return json.dumps(d,ensure_ascii=False)

def to_json_array(l):
    return [to_json(x) for x in l]

def to_md_line(d):
    return "|\t"+"|\t".join([str(v) for _,v in d.items()])+"|"

def to_md(l,head=[],show=[]):
    if not l or not l[0]:
        return ""
    if not head:
        head = "|\t"+"|\t".join([k for k,_ in l[0].items()])+"|"
    if not show:
        show = head
    splitline = "|"+"\t|".join(["---:" for k,_ in l[0].items()])+"\t|"
    lines = [show,splitline]
    for row in l:
        line = to_md_line(row)
        lines.append(line)
    return "\n".join(lines)

def to_csv_line(d):
    return ",".join([str(v) for _,v in d.items()])

def to_csv(l,head=[],show=[]):
    if not l or not l[0]:
        return ""
    if not head:
        head = ",".join([k for k,_ in l[0].items()])
    if not show:
        show = head
    lines = [show]
    for row in l:
        line = to_csv_line(row)
        lines.append(line)
    return "\n".join(lines)

def to_xlsx(l,head=[],show=[]):
    wb = Workbook()
    ws = wb.active

    for line in to_csv(l).split("\n"):
        print(line)
        ws.append(line.split(","))

    wb.save("a.xlsx")

if __name__ == '__main__':
    console = Console()
    console.print(to_csv([{"a":1,"b":"c"},{"a":2,"b":"c"}]))
    console.print(to_xlsx([{"a":1,"b":"c"},{"a":2,"b":"c"}]))
    console.print(to_md([{"a":1,"b":"c"},{"a":2,"b":"c"}]))