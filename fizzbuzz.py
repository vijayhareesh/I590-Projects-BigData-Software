#please input the parameter while running the python file
#Execution: python fizzbuzz.py <number>
#Example execution: python fizzbuzz.py 15

from sys import argv
def fizzbuzz(num):
	newnum = 1
	while newnum<=num:
		if newnum%2==0 and newnum%3==0:
			print "fizzbuzz"
		elif newnum%2==0:
			print "fizz"
		elif newnum%3==0:
			print "buzz"
		else:
			print newnum
		newnum = newnum+1

def __main__():
	num = int(argv[1])
	fizzbuzz(num)
	#while i<=num:
	#	fizzbuzz(i)
	#	i=i+1
__main__()