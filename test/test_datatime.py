from pyboon.datetime import *

def test_datetime():
    dts = "2021-12-12 09:10:11"
    dt = datetime.datetime(2021, 12, 12, 9, 10, 11)
    assert dt == parse(dts)
    assert dts == stringify(dt)