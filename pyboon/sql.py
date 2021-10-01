import pymysql
import dataset
import re

pymysql.install_as_MySQLdb()


def get_db(url):
    return dataset.connect(url, engine_kwargs={'encoding': 'utf-8'})


def qb(l,sql):
    ret = re.search(r"SELECT (.*) FROM", sql)
    _, v = ret.group(0), ret.group(1)
    fields = v.split(",")
    print(fields)
    result = []
    for item in l:
        n = {}
        for field in fields:
            if field in item:
                n[field] = item[field]
            else:
                print(field,"not in item")
        result.append(n)
    print(result)
    return result

def qb_one(l,sql):
    ret = re.search(r"SELECT (.*) FROM", sql)
    _, v = ret.group(0), ret.group(1)
    fields = v.split(",")
    print(fields)
    result = []
    for item in l:
        n = {}
        for field in fields:
            if field in item:
                n[field] = item[field]
            else:
                print(field,"not in item")
        result.append(n)
    print(result)
    return result[0] if result else None


if __name__ == '__main__':
    qb([{"a": 1, "b": 2, "c": 3, "d": 4, }],"SELECT a,b FROM tab")
