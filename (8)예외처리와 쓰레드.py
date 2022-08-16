
import threading
import time

def sum(name, value):
    for i in range(0, value):
        print("thread", name, ":", i)
        time.sleep(0.1) 
t1 = threading.Thread(target=sum, args=('1번', 20))
t2 = threading.Thread(target=sum, args=('2번', 50))

t1.start()
t2.start()

print("Main Thread")