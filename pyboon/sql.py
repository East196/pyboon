
from pyboon import x, f

import pymysql
import dataset
import re
import os
from rich.table import Table
from rich.console import Console
console = Console()

pymysql.install_as_MySQLdb()

f.CURRENT_DIR = os.path.split(os.path.realpath(__file__))[0]
DB_URL = 'mysql://root:aFM4JrZIDgpGiqJn@localhost:3306/hello?charset=UTF8MB4'

def get_db(url):
    return dataset.connect(url, engine_kwargs={'encoding': 'utf-8'})


def info(schema="hello"):
    db = get_db(DB_URL)
    tables = db.query(f'''
SELECT 
table_schema as `schema`,
table_name as name, 
table_comment as comment
FROM information_schema.tables
WHERE table_schema = '{schema}'
ORDER BY table_name DESC;
    ''')
    tables = list(tables)
    for table in tables:
        create_table_sql = db.query(
            f"show create table {schema}.{table['name']};").next(
        )['Create Table']
        console.print(table)
        console.print(create_table_sql)
        table['sql'] = create_table_sql
        columns = db.query(f'''
Select 
COLUMN_NAME as name, 
DATA_TYPE as dtype, 
character_maximum_length as length,
is_nullable as nullable, 
COLUMN_DEFAULT as value, 
COLUMN_KEY as keytype,
extra,
ordinal_position as idx, 
COLUMN_COMMENT as comment
from INFORMATION_SCHEMA.COLUMNS
Where table_name = '{table['name']}'
AND table_schema = '{schema}'
    ''')
        columns = list(columns)
        for column in columns:
            column['table'] = table['name']
            column['schema'] = schema
        table['columns'] = columns
        # console.print(json.dumps(table, ensure_ascii=False))
    return tables


def p():
    tables = info()
    for table in tables:
        columns = table['columns']
        # console.print(table,"green")
        ctable = Table()
        for k, v in columns[0].items():
            ctable.add_column(f'[red]{k}')
        for column in columns:
            ctable.add_row(*[f'[yellow]{v}' for k, v in column.items()])
        console.print(ctable)


def t(comment, table, schema='hello'):
    db = get_db(DB_URL)
    return db.query(f"alter table {schema}.{table} comment '{comment}';")


def c(comment, column, table="hello_holiday", schema='hello'):
    db = get_db(DB_URL)
    coltype = db.query(f'''
Select 
COLUMN_NAME as name, 
COLUMN_TYPE as coltype
from INFORMATION_SCHEMA.COLUMNS
Where table_name = '{table}'
AND table_schema = '{schema}'
AND COLUMN_NAME = '{column}'
    ''').next()['coltype']
    return db.query(f"ALTER TABLE {schema}.{table} MODIFY {column} {coltype} COMMENT '{comment}';")


def todb():
    db = get_db(DB_URL)
    meta_column = db['meta_column']
    meta_column.insert_many([column for table in info()
                            for column in table['columns']])
    meta_table = db['meta_table']
    meta_table.insert_many(
        [dict(name=table['name'], comment=table['comment']) for table in info()])

def tm():
    models = []
    for table in info():
        model: dict = dict(model=table['name'], Model=x.to_pascal(
            table['name']), modelCN=table['comment'])
        if 'fields' not in model:
            model['fields'] = []
        # print(model)
        for column in table['columns']:
            field = dict(
                name=column['name'], type=column['dtype'], comment=column['comment'],pk=column['name']=='id')
            # print(field)
            model['fields'].append(field)
        models.append(model)
    return models    
    
def qb(l, sql):
    ret = re.search(r"SELECT (.*) FROM", sql)
    if ret is None:
        raise ValueError("Invalid SQL query")
    _, v = ret.group(0), ret.group(1)
    fields = [field.strip() for field in v.split(",")]
    print(fields)
    result = []
    for item in l:
        n = {}
        for field in fields:
            if field in item:
                n[field] = item[field]
            else:
                print(field, "not in item")
        result.append(n)
    print(result)
    return result


def qb_one(l, sql):
    ret = re.search(r"SELECT (.*) FROM", sql)
    if ret is None:
        raise ValueError("Invalid SQL query")
    _, v = ret.group(0), ret.group(1)
    fields = [field.strip() for field in v.split(",")]
    print(fields)
    result = []
    for item in l:
        n = {}
        for field in fields:
            if field in item:
                n[field] = item[field]
            else:
                print(field, "not in item")
        result.append(n)
    print(result)
    return result[0] if result else None


if __name__ == '__main__':
    qb([{"a": 1, "b": 2, "c": 3, "d": 4, }], "SELECT a,b FROM tab")
    info()
    p()
    tm()
    t('表', "meta_table", schema='hello')
    c('名称', 'name', table="meta_table", schema='hello')
    c('注释', 'comment', table="meta_table", schema='hello')
    # todb()