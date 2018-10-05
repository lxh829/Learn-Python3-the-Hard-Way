print("I am %d years old."%20)   
print("I am %s years old."%20)
print("I am %r years old."%20)

text = "I am %d years old."%20
print("I said: %s."%text)#%s仅仅是将text中的字符串带入到字符串中
print("I also said: %r."%text)#%r是将text中的所有元素带入到字符串，包括引号传入的过程中，使用单引号来表示

import datetime
d = datetime.date.today()
print("%s"%d)
print("%r"%d)
