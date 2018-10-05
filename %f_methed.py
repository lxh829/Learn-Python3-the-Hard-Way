## %f的用法
import math

import datetime
a = datetime.date.today()
print(a)


num = math.pi
print("number = %f"%num)	#number = 3.141593
print("number = %9f"%num)	#number =  3.141593
print("number = %03.f"%num)	#number = 003
print("number = %6.3f"%num)	#number =  3.142
print("number = %-6.3f"%num)	#number = 3.142 
print("number = %15.7f"%num)	#number =       3.1415927
print("number = %015.7f"%num)	#number = 0000003.1415927
