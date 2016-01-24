from sys import argv
#please input the parameter while running the python file
#Execution: python fizzbuzz.py <number>
#Example execution: python fizzbuzz.py 15

def fizzbuzz(newnum):
	if newnum%2==0 and newnum%3==0:
		print "fizzbuzz"
	elif newnum%2==0:
		print "fizz"
	elif newnum%3==0:
		print "buzz"
	else:
		print newnum

def __main__():
	num = int(argv[1])
	i=1
	while i<=num:
		fizzbuzz(i)
		i=i+1
__main__()