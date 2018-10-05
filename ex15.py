###通过argv的方式来读取文件名，并将文件名中的内容显示出来。
from sys import argv			#从sys模块中导入arguement variable(参数变量)
script, filename = argv			#解包２个参数，一个脚本参数，另一个是文件名参数

txt = open(filename)#使用open()函数来获取文件名，filename是从命令行输入后通过filename = sys.argv[1]来传递过来的


print("Here's your file %s:."%filename)#打印出来你从命令行输入的文件名称，用来查看
print(txt.read())	#获取到文件名称后，通过使用read()函数来读取文件名中的内容与less ex15_sample.txt一样
txt.close()


###通过input()函数来将文件名读取出来
print("Type the filename again:",end=' ')#在一次输入你的文件名
file_again = input(">")#通过input()，用户通过命令行输入想要读取的文件名称并将它传递给变量file_name

txt_again = open(file_again)#通过open()函数来进行文件的打开，再通过read()函数将文件名中的内容读出来

print(txt_again.read())
txt_again.close()
