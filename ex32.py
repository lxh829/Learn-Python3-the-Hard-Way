the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in the_count:
	print("This is count %s."%number)
	print("xxx")
#same as above 与上面相同
for fruit in fruits:
	print("A fruit of type: %s."%fruit)
	print("vvv")
#also we can go through mixed lists too
#notice we have to use %s since we don't know what's in it我们不知道里面是什么，需要时用%s来看清楚
for i in change:
	print("I got %s."%i)
	print("nnn")
#we can also build lists, first start with an emply one
elements = []
#then use the range function to do 0 to 5 counts
for i in range (0, 6):
	print("Adding %s to the list."%i)
	print("ggg")
	#append is a function that lists understand
	elements.append(i)
#now we can print them out too
for i in elements:
	print("element was: %s."%i,end=' ')
	print("...")


