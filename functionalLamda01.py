def myNum(x):
	return lambda a : a * x

doubleNum = myNum(2)
print(doubleNum(11))

tripleNum = myNum(3)
print(tripleNum(11))	 