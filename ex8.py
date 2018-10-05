import datetime
date = datetime.datetime.today()
print(date)  #print now time

##格式完完全全全按照formatter变量中的格式来
formatter1 = "{1}{0}{3}{2}";formatter2 = "{1} {0} {3} {2}"
print(formatter1.format('T','E','S','B')) 	#result:TESB
print(formatter2.format('T','E','S','B'))	#result:T E S B

formatter = "{} {} {}{}"
print(formatter.format(1,2,3,4))	#result:1 2 34
print(formatter.format("one","two","three","four"))	#result:one two threefour
print(formatter.format(True,False,"True","False"))  #result:True False TrueFalse
print(formatter.format(formatter,formatter,formatter,formatter)) #result:{} {} {}{} {} {} {}{} {} {} {}{} {} {} {}{} 
print(formatter.format("Try your",
"Own text here",
"Maybe a poem ",
"Or a song sbout fear.")) #result:在这里试试你自己的文字也许是一首是或者一首关于恐惧的歌


print("{2}:计算机在{0}的cpu　占用率高达{1}%.".format(date,"10","PYTHON"))	#有一点像填空题哦

#在这里面键入空格键是会报错的，如果想要键入空格，就必须要使用Ｔａｂ按键来进行缩进。
