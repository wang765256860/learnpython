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
# from io import StringIO

# f = StringIO('hello world')
# print(f.read())

"""
pickle dump
"""
# import pickle

# d = {'name':'wangzhen','age':12}
# f = open('/Users/wangzhen/learnpython/IO编程/pickle.txt','wb')
# pickle.dump(d,f)
# f.close()
"""
pickle load
"""
# import pickle

# f = open('/Users/wangzhen/learnpython/IO编程/pickle.txt','rb')
# d = pickle.load(f)
# f.close()
# print(d)

"""
json dump
"""
# import json

# d = {'name':'wangzhen','age':12}
# f = open('/Users/wangzhen/learnpython/IO编程/json.txt','w')
# json.dump(d,f)
# f.close()

"""
json load
"""
# import json

# f = open('/Users/wangzhen/learnpython/IO编程/json.txt','r')
# d = json.load(f)
# f.close()
# print(d)


import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)


# def student2dict(std):
#     return {
#         'name': std.name,
#         'age': std.age,
#         'score': std.score
#     }


# print(json.dumps(s, default=student2dict))
g = lambda obj:obj.__dict__
print(g(s))