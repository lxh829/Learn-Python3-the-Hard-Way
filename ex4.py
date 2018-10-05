cars = 100#变量cars是100，汽车的数量是100
space_in_a_car = 4#变量space_in_a_car是4.0，每一个车中有4个空位置
drivers = 30#变量drivers是30，有30个司机
passengers = 90#变量passengers是90，有90个乘客
cars_not_driven = cars - drivers#变量cars_not_driven是变量cars的值减去变量drivers的值，没有汽车被开的数量等于总汽车的数量-司机的数量
cars_driven = drivers#变量cars_drivers的值是变量drivers的值，汽车被开的数量与司机的数量相等
carpool_capacity = cars_driven * space_in_a_car#变量carpool_capacity值是变量cars_drivers与变量space_in_a_car值的乘积，拼车容量等与汽车被开的数量乘以每一个车的空座位数
average_passengers_per_car = passengers / cars_driven#变量average_passengers_per_car的值是变量passengers与变量cars_driven，平均每一辆车上的人数等于乘客的数量除以汽车被开的数量


print("There are",cars,"cars available.")#打印出  There are 100 cars  available
print("There are only",drivers,"drivers available.")#打印 There are only 30drivers available.
print("There will be",cars_not_driven,"empty cars today.")#打印There willbr 70empty cars today.
print("We can transport(运输)",carpool_capacity,"people today.")#打印We can transport(运输) 120 people today.
print("We have",passengers,"to carpool today.")#打印We have 90 to carpool today
print("We need to put about",average_passengers_per_car,"in each car.")#打印We need to put 3.0 to in each car.
