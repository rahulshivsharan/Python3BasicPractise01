thelist = [2, "two", 3, "four"]


# for loop in python for list
for x in thelist:
	print(x)

print("The value at third position 3 is ",thelist[3])


# iterating list through for loop using range
for i in range(len(thelist)):
	print("Value at position ",i, " is ",thelist[i])


# while loop in python for list
x = 0
while x < len(thelist) :
	print("Val at position ",x, " is ",thelist[x])
	x += 1	