#隐式继承
class Parent(object):
	def implicit(self):
		print("PARENT implicit()")
class Child(Parent):
	pass
dad = Parent()
son = Child()
dad.implicit()
son.implicit()
print("- * 20")
#显式覆盖
class Parent_1(object):
	def override_1(self):
		print("PARENT override()")
class Child_1(Parent):
	def override_1(self):
		print("CHILD ocerride()")
dad_1 = Parent_1()
son_1 = Child_1()
print("- * 20")
#运行前或者运行后替换
class Parent(object):
	def altered(self):
		print("PARENT altered()")
class Child(Parent):
	def altered(self):
		print("CHILD altered()")
		super(Child, self).altered()
		print("CHILD, AFTER PARENT altered()")
dad = Parent()
son = Child()
print("-*20")
#三种方式的组合
class Parent(object):
	def override(self):
		print("PARENT override()")
	def implicit(self):
		print("PARENT implicit()")
	def altered(self):
		print("PARENT altered()")
class Child(Parent):
	def override(self):
		print("CHILD override()")
	def altered(self):
		print("CHIld, BEFORE PARENT altered()")
		super(Child,self).altered()
		print("CHILD, AFTER PARENT altered()")
