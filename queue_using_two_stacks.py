#queue using two stacks

class STACK:
	def __init__(self):
		self.top = -1
		self.stack = []

	def push(self,val):
		self.top +=1
		self.stack.append(val)

	def pop(self):

		temp = self.stack.pop(self.top)
		self.top -=1
		return temp

class QUEUE:
	def __init__(self):
		self.stack1 = STACK()
		self.stack2 = STACK()

	def enqueue(self,val):

		while self.stack2.top != -1:
			self.stack1.push(self.stack2.pop())

		self.stack1.push(val)
		
	def dequeue(self):

		while self.stack1.top != -1:
			self.stack2.push(self.stack1.pop())

		return self.stack2.pop()

	def display(self):

		while self.stack2.top != -1:
			self.stack1.push(self.stack2.pop())

		print(self.stack1.stack)
 
def main():

	Q = QUEUE()

	Q.enqueue(5)
	Q.enqueue(6)
	Q.enqueue(7)
	Q.enqueue(8)
	Q.dequeue()
	Q.dequeue()
	Q.enqueue(9)
	Q.display()

if __name__ == '__main__':
	main()