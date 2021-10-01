from pyboon.qs import *

def test_qs():
    assert 'k=v&v=%E7%BF%BB%E8%AF%91' == stringify({"k":"v","v":"翻译"})
    assert 'k=v&v=翻译' == stringify({"k":"v","v":"翻译"},u=True)
    assert {"k":"v","v":"k"} == parse('k=v&v=k')