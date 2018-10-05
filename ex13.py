from sys import argv
#read the WYSS section for how to run this
script, first, second, third,sa = argv

print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)
print("Your third variable is:",sa)
import sys

print(sys.argv)   #argv相当于是一个列表，讲命令行输入的参数全部保存到sys.argv这个列表中，方便后面的使用
