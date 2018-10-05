_metaclass_ = type	#确定使用新式类，新式类必须继承object基类，并且新式类提供了对象的方法和静态方法的支持  meta基 class 类
class TestEncapsulation(object):
	def __init__(self):#构造函数，在程序启动时自动调用，一般作为实例化对象的
		self.statement = "Start"
		print(self.statement)
	def accessibleMethod(self):#绑定方法，能在类外部被访问；绑定方法一定要有self形参，self表示类本身，用于传递当前类中的成员属性和方法，但是self不接受实参
		print("You can access this method",end='')
		print(self.statement)
		print("the secert message is:")
		self.__inaccessible()
	def __inaccessible(self):#私有方法，不能在类外部被访问；方法名以'__'开头
		print("You cannot access!")
	#@staticmethod
	def staticMethod():
		#self.accessibleMethod()  静态方法无法直接调用绑定方法。因为静态方法没有self形参
		print("This is a static method")
	def setStaement(self,statement):#访问器
		self.Statement = statement
	def getStatement(self):#访问器
		return self.Statement
	statement = property(fget = getStatement,fset = setStatement)#自动调用访问器设定属性
	name = "LiXiaohui"
if __name__ == "__main__":
	test = TestEncapsulation()
	test.accessibleMethod()
	test.staticMethod()
	#test.__inaccessible()  类的私有方法的命名空间只有在类的范围中，在类外不能调用
	print(TestEncapsulation.name)
	print(test.getStatement())
	test.setStatement("Just test")
	print(test.getStatement())

