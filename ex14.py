import sys
import datetime
print(datetime.datetime.today())	#print precent time
print(sys.argv)


from sys import argv
script, user_name = argv		#commend line need two variable,one is script,another is name.
prompt = '> '

print("Hi %s ,I'm the %s script."%(user_name,script))	#Hi V[1],I'm the ex14.py script.
print("I'd like to ask you a few questions.")		#I'd like to ask you afewquestions.
print("Do you like me %s?"%user_name,end=' ')		#Do you like me name?use space to instead \n > input your answer
likes = input(prompt)

print("Where do you live %s?"%user_name,end=' ')	#Where do you live name? use space to instead \n > input your answer
lives = input(prompt)

print("What kind of computer do you have?",end=' ')	#What kind of computer do you have? use space to instead \n input your answer
computer = input(prompt)

print("""
\tAlright,so you said %s about liking me.
\tYou live in %s.Not sure where that is.
\tAnd you have a %s computer. Nice."""%(likes,lives,computer))
