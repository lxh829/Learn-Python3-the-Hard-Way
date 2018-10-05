people = 30
cats = 40
trunks = 15

if cats > people:
	print("We should take the cars.")
elif cats < people:
	print("We should not take the cars.")
else:
	print("We can't decide.")
	
if trunks > cats:
	print("That's too many trunks.")
elif trunks < cats:
	print("Maybe we could take the trunks.")
else:
	print("We still can't decide.")

if people > trunks:
	print("Alright,let's just take the trunks.")
else:
	print("Fine,let's stay home then.")
