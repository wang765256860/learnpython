import os

cur_path = os.path.dirname(os.path.abspath(__file__))
print(cur_path)
x = [x for x in os.listdir(cur_path)]
for i in x:
    print(i)
