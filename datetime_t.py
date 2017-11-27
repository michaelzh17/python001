# -*- coding:utf-8 -*-

#string to timestamp


import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    #change datetime_string to date time
    dt = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')

    #get timezone information
    #re.match(r'^(\w{3})\+(\d{1,2}):(\d{2})$','UTC+12:00')
    #re.match(r'^(\w{3})-(\d{1,2}):(\d{2})$','UTC-12:00')
    #re.match(r'^(\w{3})([+-])(\d{1,2}):(\d{2})$','UTC+12:00')
    #tz = re.match(r'^(\w{3})\+(\d{1,2}):(\d{2})$',tz_str)
    tz = re.match(r'^(\w{3})([+-])(\d{1,2}):(\d{2})$',tz_str)
    print(dt)
    print(tz.group(0))
    if tz.group(2) == '+':
        tz_utc_x = timezone(timedelta(hours=int(tz.group(3))))
        ts = dt.replace(tzinfo=tz_utc_x)
        #ts = dt.astimezone(timezone(timedelta(hours=int(tz.group(3)))))
    if tz.group(2) == '-':
        tz_utc_x = timezone(timedelta(hours=-int(tz.group(3))))
        ts = dt.replace(tzinfo=tz_utc_x)
    return ts.timestamp()



#testing


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('Pass')
