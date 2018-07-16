import itertools
from functools import reduce

def pi(N):
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    odd = itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    odd_N = list(itertools.takewhile(lambda x:x<=2*N-1,odd))
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    """方案一"""
    # i = 0
    # s = 0
    # for n in odd_N:
    #     i += 1
    #     if i%2 == 0:
    #         n = -n
    #     # step 4: 求和:
    #     s += 4/n
    # return s
    """方案二"""
    sub1 = map(lambda x:4/x,odd_N[0::2])
    sub2 = map(lambda x:-4/x,odd_N[1::2])
    sub = reduce(lambda x,y:x+y,sub1)+reduce(lambda x,y:x+y,sub2)
    return sub
plus = pi(10000)
print(plus)
    