from sys import argv#从sys模块中导入参数变量
script, input_file = argv#将参数变量argv解包乘２个命令行参数，并将这２个参数存放到列表argv中，排列从0位置开始，以此类推

def print_all(f):#定义函数print_all()，里面只包含一个参数f
	print(f.read())#对参数f(应该是个文件)进行读取，并打印出来

def rewind(f):#定义函数rewind()，倒带，同样函数里面只有一个变量f
	print(f.tell())#返回值会告诉你当前文件的游标位置
	print(f.seek(0))#对f进行seek()函数操作，seek(0)函数的处理对象是字节并非行，seek(0)只是转到文字文件的0字节，也就是第一个文字的位置

def print_a_line(line_count, f):#定义函数print_a_line(),此函数有２个参数，一个是行的数字，另一个是f变量
	print(line_count, f.readline())#打印出变量line_count,f.readline()此函数作用是将文件的内容以行来读出来，它会扫描文件的每一个字节，直到找到一个\n(换行符)为止，然后停止读取文件，并且返回此前发现的文件内容，文件f会记录每次调用readline()后的读取位置，这样他就可以在下次被调用时读取接下来的一行了。

current_file = open(input_file)#以读的方式来打开文件
print("First let's print the whole file:")#print出来整个文件内容
print_all(current_file)#调用函数print_all(),通过read()函数来读取文件内容并打印出来

print("Now let's rewind, kind of like a tape.")#来到带，就像一个磁带通过磁头来读取数据
rewind(current_file)#通过调用current_file()函数，来寻找文件的第０个字节所在的位置买也就是第一个字所在的位置，并非第２行

print("Let's print three lines:")#print　３行
current_line = 1	#目前的行数
print_a_line(current_line, current_file)#调用函数print_a_line(),打印出行数以及行数相对应的内容

current_line = current_line + 1#来到第二行
print_a_line(current_line, current_file)#同样的道理，调用函数来大银行数以及行数对应的内容

current_line =current_line + 5
print_a_line(current_line, current_file)#同上
