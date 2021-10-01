import time
import datetime

def stringify(dt):
    return time.strftime("%Y-%m-%d %H:%M:%S",dt.timetuple())

def parse(s):
    return datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
    