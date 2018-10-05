types_of_people = 10.00
x = "there are %s types of people."%types_of_people
x_ = "There are %s type of people."%20.00
print(x)
print(x_)
print("I said: %r."%x)

binary = "binary(二进制)"
do_not = "don't"
y = "Those who know %s and those who %s."%(binary,do_not)
print(y)
print("I also said:%s and %r and %r."%(y,x,x_))

hilarious = "False"
joke_evalation = "Isn't that joke so funny?! %r"
print(joke_evalation %binary)

w = "This is the left side of..."
e = "a string with a right side."
print(w+e)

