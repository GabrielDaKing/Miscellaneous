#random_number_infinite_stream

import random
from collections import Counter

number_stream = [x for x in range(500)]

def random_number(stream):

	selection = -1

	for i in range(len(number_stream)):

		rand = random.random()

		if rand<1/(i+1):
			selection = number_stream[i]

	return selection

def main():

	print(random_number(number_stream))

	# Run the below function for proof of the proper working of this program
	#testing()

	
def testing():

	result = []

	for i in range(1000000):
			
		print(i)
		t = random_number(number_stream)
		result.append(t)
	
	print(dict(Counter(result)))


if __name__ == '__main__':
	main()