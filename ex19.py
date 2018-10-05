#函数会将传递的值打印出来，我们可以直接给函数传递数字，也可以给他变量，还可以给她数学表达式，甚至可以把数学表达式和变量组合起来用。从一方面来说，函数的参数和生成变量时用的＝与赋值符类似，事实上如果一个物件可以用＝对其命名，通常也可以将它作为参数传递给一个函数。




import datetime
print(datetime.datetime.today())

#cheese 奶酪　　crackers 饼干
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print("You have %s cheeses!"%cheese_count)
	print("You have %s boxes of crackers!"%boxes_of_crackers)
	print("Man that's enough for a party!")
	print("Get a blanket.",end='\n')

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR,we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)

print("And we can combine the two, variable and math:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers + 1000)
