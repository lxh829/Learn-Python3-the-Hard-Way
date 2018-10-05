#this one is like your scripts with argv 这个就像你的参数变量脚本
def print_two(*args):
	arg1, arg2 = args
	print("arg1: %s, arg2: %s"%(arg1,arg2))

#ok,that's *args is actually pointless, we can just do this.好吧,其实*args实际上毫无意义，我们可以这样做。
def print_two_again(arg1, arg2):
	print("arg1: %s, arg2: %s"%(arg1,arg2))
#this just takes one arguments　这只需要一个参数
def print_one(arg1):
	print("arg1: %s."%arg1)

#this one takes no arguments 这一个不带任何参数
def print_none():
	print("I got nothin'.")#我什么也没得到

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()
