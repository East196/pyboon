from urllib.parse import urlencode,parse_qs,unquote

def stringify(d,u=False):
    qs = urlencode(d)
    if u:
        qs = unquote(qs)
    return qs

def parse(url):
    d = dict( (k, v if len(v)>1 else v[0] )
           for k, v in parse_qs(url).items() )
    return d