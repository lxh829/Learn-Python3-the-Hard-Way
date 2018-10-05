ten_things = "Apples Oranges Crows Telephone Light Sugar"#将字符串输入给变量

print("Wait ther are not 10 things in that list .Let's fix that.")#print string
stuff = ten_things.split(' ')#切片，以空格为分隔符，讲字符串分割为多个字符串，并存入列表stuff中
print(stuff)#打印变量stuff
print(ten_things)#打印变量ten_things
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']#this is a list

while len(stuff) != 10:#循环，直到变量stuff的长度等于10为止，一共循环４次
	print(len(stuff))#6,7,8,9
	next_one = more_stuff.pop()#pop 弹出，默认为弹出列表的最后一个，如果有参数则为索引值
	print("Adding: ",next_one)#打印出弹出来的列表中的元素
	stuff.append(next_one)#讲弹出来的列表中的元素加入到stuff列表的末尾
	print(stuff)#打印变量stuff
	print("There are %s items now."%len(stuff))
print("There we go: ", stuff)
print("Let's do some things with stuff.")

print(stuff[1])#打印列表stuff的位置１处的元素，也是索引值为１
print(stuff[-1])#whoa!fancy哇，花哨，索引值为－１是打印列表的最后一个元素
print(stuff.pop())#pop默认弹出列表的最后一个元素
print(' '.join(stuff))#what? cool!将列表中的元素以空格来连接形成一个字符串
print('#'.join(stuff[3:5]))#supper stellar切片操作，左闭右开
