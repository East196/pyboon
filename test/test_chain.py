from pyboon.chain import Chain
from pyboon import __

def test_chain():
    items = [1,2,3]
    chain = Chain(items)
    assert [1,2,3] == chain.items
    assert [1,2,3] == chain.to_list()
    assert 1 == chain.first()
    assert 2 == chain.map(lambda x:x+1).first()
    assert 2 == __.chain(items).map(lambda x:x+1).first()