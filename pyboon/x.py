import datetime
import json
import time
import requests
from rich.table import Table
from rich.console import Console
from rich.syntax import Syntax


def highlight(code, language="python"):
    if type(code) is dict or type(code) is list:
         code = json.dumps(code, indent=2, ensure_ascii=False)
    syntax = Syntax(code, language)
    console = Console()
    console.print(syntax)

def print_table(dicts):
    ctable = Table()
    for k, v in dicts[0].items():
        ctable.add_column(f'[red]{k}')
    for column in dicts:
        ctable.add_row(*[f'[yellow]{v}' for k, v in column.items()])
    console = Console()
    console.print(ctable)

def to_table(dicts):
    import prettytable as pt
    tb = pt.PrettyTable()
    tb.field_names = [k for k, _ in dicts[0].items()]
    for column in dicts:
        tb.add_row([v for k, v in column.items()])
    return tb.get_string()


def to_dict(s):
    return json.loads(s, encoding="UTF8")


def to_json(d):
    return json.dumps(d, ensure_ascii=False)


def now_time_str():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def delta_time_str(**delta):
    return (datetime.datetime.now() + datetime.timedelta(**delta)).strftime("%Y-%m-%d %H:%M:%S")


def to_time_str(t):
    return time.strftime("%Y-%m-%d %H:%M:%S", t)


def to_local_time(s):
    return time.strptime(s, "%Y-%m-%d %H:%M:%S")


def to_time_ms(s):
    return int(time.mktime(to_local_time(s)) * 1000)


def now_ms():
    return int(time.time() * 1000)


def to_seq(s):
    text = s.strip()
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)

    return "".join(lst).lower().replace("__", " ").replace("_", " ")


def to_pascal(s):
    us = to_seq(s)
    tus = us.title().replace(" ", "")
    return tus


def to_camel(s):
    us = to_seq(s)
    tus = us.title().replace(" ", "")
    return tus[:1].lower()+tus[1:]


def to_underscore(s):
    us = to_seq(s)
    return us.replace(" ", "_")


def to_minus(s):
    us = to_seq(s)
    return us.replace(" ", "-")

def to_html(md):
    import markdown
    html = markdown.markdown(md, extensions=['tables'])
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    return soup.prettify()


def translate(query):
    url = 'http://fanyi.youdao.com/translate'
    payload = {'doctype': "json", 'type': "AUTO", 'i': query}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
    r = requests.get(url, params=payload, headers=headers)
    result = r.json()["translateResult"][0][0]["tgt"]
    return result


if __name__ == '__main__':
    highlight('''import rich''')
    print(to_seq("HelloNew_world"))
    print(to_pascal("HelloNew_world"))
    print(to_camel("HelloNew_world"))
    print(to_underscore("HelloNew_world"))
    print(to_minus("HelloNew_world"))
