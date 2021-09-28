from pyboon.x import *

def test_to_camel():
    assert 'helloNewWorld' == to_camel("HelloNew_world")