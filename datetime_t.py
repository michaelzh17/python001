# -*- coding:utf-8 -*-

#string to timestamp


import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    #change datetime_string to date time
    tr = datetime.strftime(dt_str, '%Y-%m-%d %H:%M:%S')

