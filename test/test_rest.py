from pyboon.rest import *


def test_rest():
    assert {"a": '1'} == get("http://httpbin.org/get", {"a": '1'})['args']
    assert {"a": '1'} == post("http://httpbin.org/post", {"a": '1'})['json']
    assert {"a": '1'} == json("http://httpbin.org/post", {"a": '1'})['json']
    assert {"a": '1'} == form("http://httpbin.org/post", {"a": '1'})['form']
