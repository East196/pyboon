from pyboon.x import *

def test_to_xxx():
    assert 'hello new world' == to_seq("HelloNew_world")
    assert 'HelloNewWorld'   == to_pascal("HelloNew_world")
    assert 'helloNewWorld'   == to_camel("HelloNew_world")
    assert 'hello_new_world' == to_underscore("HelloNew_world")
    assert 'hello-new-world' == to_minus("HelloNew_world")