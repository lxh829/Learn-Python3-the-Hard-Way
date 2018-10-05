def add(a, b):
	print("Adding: %d + %d"%(a, b))
	return a+b	

def subtract(a, b):
	print("Subtracting: %s - %s"%(a, b))
	return a-b

def multiply(a, b):
	print("Multiplying: %s * %s"%(a, b))
	return a*b

def divide(a, b):
	print("Dividing: %d / %d"%(a, b))
	return a/b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print("Age: %s\nheight: %d\nweight: %s\niq: %s\n"%(age, height, weight, iq))

#A puzzle for the extra credit,type it in anyway.(一个困惑对于额外的信用，无论如何键入它)
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))	# -4391
print("That becomes: ", what ,"Can you do it by hand?")
