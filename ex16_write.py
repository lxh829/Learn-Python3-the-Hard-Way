filename = input("请输入你想要写入的文件：")
find_filename = open(filename,'a')
content = """\t人生就像一块拼图，认识一个人越久越深，这幅图就越完整。
\t但始终\n无法看到全部，因为每一个人都是一个谜，没必要一定看透，却总也看不完。"""
find_filename.write(content)
find_filename.close()
