import sys#导入sys模块
script, encoding, error = sys.argv#将命令行参数解包为３个参数


def main(language_file, encoding, errors):#定义函数，切此函数有三个参数
	line = language_file.readline()#将文件按行来读取，关键代码从这个叫main的的主函数开始，该函数会在脚本的结尾调用。

	if line:#if条件语句，如果　line　为真，则向下运行，如果为假则跳出词条语句.这是一个if语句，你可以用它在python代码中做出决策，你可以检验一个变量的真值。给予这一真值来决定一段代码运行与否，当运行到文件结尾时readline函数会返回一个空字符串，这行if就是用来检查这个空字符串的，只要readline返回了内容，这里就是为真下面２行缩进的代码就会执行，如果他为假，则下面的２行代码会被跳过。
		print_line(line, encoding, errors)#调用函数print_line()
		return main(language_file, encoding, errors)#返回值，在main函数里面调用了一次main,其实在函数里面调用函数，从技术上讲不管函数在哪里，我们都是可以调用的，连主函数也不例外，如果函数只是跳转到这个这个叫main的位置，那么调用函数自己只不过是跳转到函数顶端在运行一次而已，这样其实就是一个循环了


def print_line(line, encoding, errors):#定义函数print_line()，且有三个参数
	next_lang = line.strip()#将每一行的换行符\n删除
	raw_bytes = next_lang.encode(encoding, errors = errors)#得到了language.txt中的语言，把它编码成原始字节，DBES:解码字符串,编码字符串，next_lang变量是一个字符串，要获取原始字节串。需要调用编码字符串，需要把编码方式和处理错误的方式传入encode()函数。
	cooked_string = raw_bytes.decode(encoding, errors = errors)#额外的一部，展示了上一行的逆操作，从raw_bytes创建一个cooked_string变量，raw_bytes就是字节串，所以调用了decode()，从而得到一个python字符串，这个字符串是和next_lang变量是一样的。

	print(raw_bytes, "<==>", cooked_string)


languages = open("ex23_languages.txt", encoding = "utf-8")

main(languages, encoding, error)
