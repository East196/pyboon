from pyboon.sql import *

def test_sql():
    db = get_db('mysql://root:aFM4JrZIDgpGiqJn@localhost:3306/hello?charset=UTF8MB4')
    assert 1 == db.query('select 1 from dual').next()['1']

def test_qb():
    assert [{'a': 1, 'b': 2}] == qb([{"a":1,"b":2,"c":3,"d":4,}],"SELECT a,b,e FROM tab")
    assert {'a': 1, 'b': 2} == qb_one([{"a":1,"b":2,"c":3,"d":4,}],"SELECT a,b,e FROM tab")