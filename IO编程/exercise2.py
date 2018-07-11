from datetime import datetime
import os

pwd = os.path.abspath('.')
list_dir = os.listdir(pwd)
print('\tSize\t Modified time\t\tName')
print('-'*50)

for i in list_dir:
    i_size = os.path.getsize(i)
    mdf_time = datetime.fromtimestamp(os.path.getmtime(i)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isfile(i) else ''
    print('\t%d\t%s\t%s%s' %(i_size,mdf_time,i,flag))