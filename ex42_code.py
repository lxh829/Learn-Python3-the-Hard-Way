#Animal is-a object
class Animal(object):
	pass
#Dog is a Animal(Dog inherits the parent class Animal)
class Dog(Animal):
	def __init__ (self, name):
		#Dog has-a name
		self.name = name
#Cat is a Animal(Cat inherits the parent class Animal)
class Cat(Animal):
	def __init__(self, name):
		#Cat has a name
		self.name = name
#Person is a object
class Person(object):
	def __init__(self, name):
		#Person has a name
		self.name = name
		#Person has a pet
		self.pet = None
#Employee is a Person
class Employee(Person):
	def __init__(self, name, salary):
		#调用它的父类Person()来初始化,Person has a name
		super(Employee, self).__init__(name)
		#Employee has a salary
		self.salary = salary
#Fish is a object
class Fish(object):
	pass
#Salmon is a Fish(Salmon inherits the parents Fish)
class Salmon(Fish):
	pass
#Halibut is a Fish(Halibut inherits the parents Fish)
class Halibut(Fish):
	pass
#rover is a Dog,rover是Dog实例化后的一个对象
rover = Dog("Rover")
#santan is a Cat,santon是Cat实例化后的一个对象
santon = Cat("Santon")
#mary is a Person,mary是Person实例化后的一个对象
mary = Person("mary")
#mary has a attribute pet and be defined to saton
mary.pet = saton
#frank is a Employee,frank是Employee实例后的一个对象
frank = Employee("Frankk", 120000)
#flipper is a Fish
flipper = Flsh()
#crouse is a Salmon
crouse = Salmon()
#harry is a Halibut
harry = Halibut()
