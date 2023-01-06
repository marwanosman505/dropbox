import threading

class bar():
	def __init__(self):
		self.counter = 0
		self.threadlock = threading.Lock()
	def foo(self, x):
		self.threadlock.acquire()
		for i in range(x):
			self.counter += 1
		self.threadlock.release()

mybar = bar()
print(mybar.counter)

x = threading.Thread(target=mybar.foo, args=(100000,))
y = threading.Thread(target=mybar.foo, args=(100000,))
x.start()
#x.join()
y.start()
#y.join()
print(mybar.counter)

