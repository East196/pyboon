import json


def stringify(d):
    return json.dumps(d, ensure_ascii=False)


def prettify(d):
    return json.dumps(d, indent=2, ensure_ascii=False)


def parse(json_str):
    d = json.loads(json_str)
    return d
