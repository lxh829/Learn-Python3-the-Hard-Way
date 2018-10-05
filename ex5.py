###line1-7均是将变量赋值
my_name = "lixiaohui"
my_age = 23
my_height_inches = 70 ;my_height_cm = 2.54 * my_height_inches     #1 inches == 2.54 cm
my_weight_lbs = 112 ;my_weight_kg = 0.454 * my_weight_lbs         #1 lbs(英镑) == 0.454 kg
my_eyes = 'black'
my_teeth = 'White'
my_hair = 'black'

print("Let's talk about %s." %my_name)#格式化字符串文字，仅仅只能使用%s来，如果有多个%s，则需要使用%(s1,s2,s3,...,sn),例子可以看line19 and line14
print("He's %s inches tall."%my_height_inches);print("He's %s centimeter tall."%my_height_cm)
print("He's %s pounds equalto %s kilogram heavy."%(my_weight_lbs,my_weight_kg))
print("Actully that's not too heavy.")
print("He's got %s eyes and %s hair ."%(my_eyes,my_hair))
print("His teeth are usually %s depending on the coffee."%my_teeth)

#this line is tricky ,try to get it exactly right
totle = my_age + my_height_inches + my_weight_lbs
print("If I add %s,%s,and %s I get."%(my_age,my_height_inches,my_weight_lbs))


a = 1.222
b = 1.5699
a_ = round(a)
b_ = round(b)
print("%s %s."%(a_,b_))
