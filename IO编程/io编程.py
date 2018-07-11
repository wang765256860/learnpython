"""
with open('/Users/wangzhen/learnpython/IO编程/abc.txt', 'w') as f:
    f.write('Hello world')
"""

"""
f = open('/Users/wangzhen/learnpython/IO编程/abc.txt','w')
f.write('what')
f.close()
"""

"""
stringio和bytesio
"""
from io import StringIO

f = StringIO('hello world')
print(f.read())