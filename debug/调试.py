
# 断言
"""
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10/n

def main():
    foo('0')

main()
"""
#*****************************
#logging
"""
import logging

s = '0'
n = int(s)
logging.basicConfig(level=logging.INFO)
logging.info('n = %d' % n)
print(10 / n)
"""
#pdb
import pdb

s = '0'
n = int(s)
print(10 / n)
dict
