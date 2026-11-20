import time
import threading

def task1():
    for i in range(5):
        print('task1 iteration',i)
        time.sleep(1)
def task2():
    for i in range(5):
        print("task2 iteration",i)
        time.sleep(1)
t1=threading.Thread(target=task1)
t2=threading.Thread(target=task2)
t1.start()
t2.start()
t1.join()
t2.join()
