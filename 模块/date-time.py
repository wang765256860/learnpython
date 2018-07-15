from datetime import datetime

n = datetime(2018,7,15,11,7,12)
print(n.timestamp())
cday = datetime.strptime('2018-10-30 11:11:11','%Y-%m-%d %H:%M:%S')
print(cday)
