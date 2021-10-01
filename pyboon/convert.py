import datetime
import json
import time

def to_int(p):
    return int(p)

def to_str(p):
    return str(p)

def to_float(p):
    return float(p)

def to_datetime(s):
    return datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")

def to_datetime_str(dt):
    return time.strftime("%Y-%m-%d %H:%M:%S",dt.timetuple())

def to_json(d):
    return json.dumps(d,ensure_ascii=False)

def to_dict(s):
    return json.loads(s)
