#suduku generator
import random
from time import sleep

numbers = [1,2,3,4,5,6,7,8,9]

random.seed(1)

class suduku:
	def __init__(self):
		self.table = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
			[-1,-1,-1,-1,-1,-1,-1,-1,-1],
			[-1,-1,-1,-1,-1,-1,-1,-1,-1],
			[-1,-1,-1,-1,-1,-1,-1,-1,-1],
			[-1,-1,-1,-1,-1,-1,-1,-1,-1],
			[-1,-1,-1,-1,-1,-1,-1,-1,-1],
			[-1,-1,-1,-1,-1,-1,-1,-1,-1],
			[-1,-1,-1,-1,-1,-1,-1,-1,-1],
			[-1,-1,-1,-1,-1,-1,-1,-1,-1]]

	def generate_suduku(self):

		self.create_top_left()
		self.create_top_mid()

	def create_top_left(self):

		numbers_available = numbers.copy()

		for i in range(3):
			for j in range(3):

				number = random.choice(numbers_available)

				numbers_available.remove(number)

				self.table[i][j] = number

	def create_top_mid(self):

		numbers_available = numbers.copy()

		for i in range(3):
			for j in range(3,6):

				flag = 0
				while flag==0:
					number = random.choice(numbers_available)
					print('testing',number)
					print(self.check_row(number,i))
					if self.check_row(number,i) and self.check_col(number,j):
						print('hello')
						self.display()
						sleep(5)
						flag=1

				numbers_available.remove(number)
				self.table[i][j] = number

	def check_row(self,number,pos_y):
		# print(self.table[pos_y])
		if number not in self.table[pos_y]:
			print('checking row')
			if pos_y%3==1n:
				if number not in self.table[pos_y+1:pos_y+3]:
			return True
		else:
			return False
		

	def check_col(self,number,pos_x):

		return True

	def display(self):

		for item in self.table:
			for ele in item:
				print(ele,end=' ')
			print()


def main():

	Suduku = suduku()

	Suduku.generate_suduku()

	Suduku.display()

if __name__ == '__main__':
	main()





