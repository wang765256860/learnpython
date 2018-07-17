import psutil

s = psutil.cpu_count(logical=False)
print(s)