import json
from rich.table import Table
from rich.panel import Panel
from rich.syntax import Syntax
from rich.console import Console
console = Console()


def highlight(code, language="python"):
    if type(code) is dict or type(code) is list:
        code = json.dumps(code, indent=2, ensure_ascii=False)
    syntax = Syntax(code, language)
    console = Console()
    console.print(syntax)


def table(dicts):
    ctable = Table()
    for k, v in dicts[0].items():
        ctable.add_column(f'[red]{k}')
    for column in dicts:
        ctable.add_row(*[f'[yellow]{v}' for k, v in column.items()])
    console.print(ctable)
