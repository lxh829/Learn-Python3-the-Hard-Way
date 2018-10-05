###  %s      #不存在补０的情况，所有的都是补空格。针对于%s的情况，对于%r也是成立的,只不过需要添加一组单引号而已。详细见 line4.
string = "Hello"
print("string = %s."%string)	#string = Hello.
print("string = %r."%string)	#string = Hello.
print("string = %2s."%string)	#string = 'Hello'.
print("string = %7s."%string)	#string =   Hello.
print("string = %-7s."%string)	#string = Hello  .
print("string = %.2s."%string)	#string = He.
print("string = %.7s."%string)	#string = Hello.
print("string = %.-7s."%string)	#string = Hello.
print("string = %1.5s."%string)	#string = Hello.
print("string = %3.2s."%string)	#string =  He.
print("string = %7.3s."%string)	#string =     Hel.
print("string = %5.8s."%string)	#string = Hello.
print("string = %05.8s."%string)	#string = Hello.
print("string = %9.05s."%string)	#string =     Hello.
print("string = %09.5s."%string)	#string = 0000Hello. 正确答案：string =     Hello 
print("string = %-09.5s."%string)	#string = Hello0000.正确答案：string = Hello    .
