import time
a=[]
for i in range(10):
	time.sleep(0.5)
	print("hello",i**3)
	a.append(i)
print(a)
