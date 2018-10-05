print("Let's  practice everything.")#打印字符串:让我们联系一些事情
print("You\'d need to know \'bout escapes with \\ that do:")#打印字符串:You'd need to know 'bout escapes with \ that do:
print("\n newlines and \t tabs.")#\n换行符，用来换行 ；\t制表符，相当与Tab键

poem = """
\tThe lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("---------")
print(poem)
print("---------")

five = 10 - 2 + 3 - 6
print("This should be five: %s."%five)

def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
start_point = 10000
beans, jars, crates = secret_formula(start_point)
#remmber that this is another way to format a string
print("With a starting point of: %s "%start_point)
#it's just like with an string
print("We'd have %s beans, %s jars, and %s crates."%(beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
#this is an easy way to apply a list to a format string
print("We'd have %s beans, %s jars,and %s crates."%(beans, jars, formula))
