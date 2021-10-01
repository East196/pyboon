from pyboon import _

def test_underscore():
    items = [1,2,3]
    assert [2,3,4] == _.map2(items,lambda x:x+1)
    assert [2,3] == _.filter2(items,lambda x:x>1)
    assert 6 == _.reduce2(items,lambda x,y:x+y)
    assert 3 == _.size(items)
    assert 6 == _.size("123456")
    assert [0] == _.range2(1)