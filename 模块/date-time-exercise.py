import re
from datetime import datetime, timedelta, timezone


def to_timestamp(dt_str,tz_str):
    ctime = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    t_zone = re.match(r'(UTC)[\+\-](\d{1,2})(\:00)',tz_str).group(2)
    t_zone = int(t_zone)
    timestp = ctime.replace(tzinfo=timezone(timedelta(hours=t_zone))).timestamp()
    return timestp
print(to_timestamp('2018-5-30 11:11:11','UTC+8:00'))