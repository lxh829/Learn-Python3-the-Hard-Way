from sys import argv#从sys中导入参数变量argement variable
from os.path import exists#从os模块的path中导入exists()函数，os.path.exists()用来判断指定路径中的文件是否存在，存在返回真True,不存在则返回False。

script, from_file, to_file = argv#sys.argv()讲命令行接解包为三个参数，script参数，from_file参数,to_file参数

print("Copying from %s to %s."%(from_file,to_file))#print:Copying from ex17_from_file.txt to ex17_to_file.txt

file_name = open(argv[1],'w')#以写入的方式来打开文件ex17_from_file.txt
content = """
\t如果有来生，要做一棵树。\n\t站成永恒，没有悲欢的姿势。一半在土里安详，一半在风里飞扬。\n\t一半洒落阴凉，一半沐浴阳光\n\t非常沉默，非常骄傲，从不依靠，从不寻找。 """#你需要写入文件的内容，""" 可以随意输入，并没有其格式限制
file_name.write(content)#将content变量中的字符串写入到指定的文件中
file_name.close()#保存并关闭文件，如果没有此命令，相当于是你只是将内容写入到文件中，并没有进行保存，其实还是跟没写一样的



#We could do these two on one line,how?
in_file = open(from_file)#以r的方式来打开文件
indata = in_file.read()#通过使用read()函数来将from_file中的内容来或取出来保存到indata变量中

print("The input file is %.2f bytes long."%len(indata))#使用len()函数来得到indata变量中的字节数，也就是大小

print("Does the output file exist? %s"%exists(to_file))#使用exist()函数来判断路径中是否存在to_file变量中的文件，如果存在返回True,如果不存在则返回False.
print("Ready,hit RETURN to continue, CTRL-c to abort")#print:Ready,hit RETURN to continue.
input()

out_file = open(to_file,'w')#打开文件用写的方式，意识告诉程序，哥要开始写讲文件中写东西了
out_file.write(indata)#通过write()函数来将变量indata中的内容写入到out_file变量中的文件中

print("Alright, all done.")#print:Alright,all done.好了，所有的已经完成了。

out_file.close()#使用close()函数来保存，文件并关闭
in_file.close()#同样的道理
