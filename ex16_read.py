#import sys
#script, filename = sys.argv
#content = open(filename)
#a = content.read()
#print(a)

filename = input("请输入你想要打开的文件名：")
find_file = open(filename)
content = find_file.read()
print(content)
