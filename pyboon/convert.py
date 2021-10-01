import datetime
import json
import time
import yaml
import re


def to_int(p):
    return int(p)


def to_str(p):
    return str(p)


def to_float(p):
    return float(p)


def to_datetime(s):
    return datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")


def to_datetime_str(dt):
    return time.strftime("%Y-%m-%d %H:%M:%S", dt.timetuple())


def to_yaml(d):
    content = yaml.dump(d, default_flow_style=False)
    content = re.sub(r'(\\u[a-zA-Z0-9]{4})', lambda x: x.group(
        1).encode("utf-8").decode("unicode-escape"), content) # 逐段解码
    return content


def to_json(d):
    return json.dumps(d, ensure_ascii=False)


def to_dict(s):
    # return json.loads(s)
    return yaml.load(s, Loader=yaml.FullLoader)
