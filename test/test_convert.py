from pyboon.convert import *

def test_convert():
    dts = "2021-12-12 09:10:11"
    dt = datetime.datetime(2021, 12, 12, 9, 10, 11)
    assert dt.timetuple() == time.strptime(dts, "%Y-%m-%d %H:%M:%S")
    assert dts == time.strftime("%Y-%m-%d %H:%M:%S",dt.timetuple())
    assert dt == to_datetime(dts)
    assert dts == to_datetime_str(dt)
    assert 1 == to_int('1')
    assert 1.0 == to_float('1')
    assert '1' == to_str(1)
    assert '1.0' == to_str(1.0)
    assert {"k":"v","v":"汉字"} == to_dict('{"k":"v","v":"汉字"}')
    assert '{"k": "v", "v": "汉字"}' == to_json({"k":"v","v":"汉字"})