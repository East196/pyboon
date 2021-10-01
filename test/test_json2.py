from pyboon.json2 import *

def test_json():
    assert {"k":"v","v":"汉字"} == parse('{"k":"v","v":"汉字"}')
    assert '{"k": "v", "v": "汉字"}' == stringify({"k":"v","v":"汉字"})