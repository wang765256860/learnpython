# import os 

# print('Process (%s) start '%os.getppid())

# pid = os.fork()
# if pid  == 0:
#     print('1')
# else:
#     print('2')
"""
multiprocessing
"""
# from multiprocessing import Process
# import os
# def run_proc(name):
#     print('Run child process %s (%s)'%(name,os.getpid()))

# if __name__ == '__main__':
#     print('Parent process %s '%os.getpid())
#     p = Process(target=run_proc,args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')
"""
Pool
"""
# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(6)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')

"""
subprocess
"""
# import subprocess

# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup','www.python.org'])
# print('Exit code:',r)

"""
进程间通信
"""
# from multiprocessing import Process, Queue
# import os, time,random

# def write(q):
#     print('Process to write %s'%os.getpid())
#     for value in ['A','B','C']:
#         print('Put %s to queue'%value)
#         q.put(value)
#         time.sleep(2)

# def read(q):
#     print('Process to write %s'%os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue'%value)

# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write,args=(q,))
#     pr = Process(target=read,args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()