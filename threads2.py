# Race condition 
# Deadlock 


import threading
print(dir(threading.Thread))
import time 
def square(num):
	global count    
	print("Inside square")
    # time.sleep(10)
    # print(num*num)
	lock.acquire()
	lock.acquire()
	
	print("{}acquired lock".format(threading.current_thread().getName()))
	for value in range(5):
		count+= 10
		time.sleep(2)
		print(count)
	lock.release()
	lock.release()
	print("{}released lock".format(threading.current_thread().getName()))
    
def multiply(num1,num2):
	global count
	print("Inside multiply")
    # print(num1*num2)
	# lock.release()
	lock.acquire()
	print("{}acquired lock".format(threading.currentThread().getName()))
	for value in range(5):
		count+= 2
		time.sleep(1)
		print(count)
	lock.release()
	print("{}released lock".format(threading.currentThread().getName()))

count = 100
lock = threading.RLock()
# lock = threading.Semaphore(2)

# print(dir(threading))

t1 = threading.Thread(target=square,args = (5,),name = "t1")
t2 = threading.Thread(target = multiply,args = (5,6),name = "t2")

# t3 = threading.Thread(target=square,args = (5,),name = "t3")
# t4 = threading.Thread(target = multiply,args = (5,6),name = "t4")

# t5 = threading.Thread(target=square,args = (5,),name = "t5")
# t6 = threading.Thread(target = multiply,args = (5,6),name = "t6")


t1.start()
t2.start()

# t3.start()
# t4.start()
# t5.start()
# t6.start()


