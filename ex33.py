import datetime
a = datetime.datetime.today()
print(a)#此行是打印出目前为止的时间
#While loop
i = 0
numbers = []#新建一个列表，元祖是不能改变的列表
while i < 6:
	print("At the top i is %s."%i)
	numbers.append(i)#将变量中的i添加到列表中
	
	i += 1
	print("Numbes now: ",numbers)
	print("At the bottom i is %s."%i)
print("The numbers: ")
for i in numbers:#for 循环i等于一个值来运行一次对应的代码块，有多少次就循环多少次
	print(i)
