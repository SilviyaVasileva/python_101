
class Bill:
	def __init__(self, amount):
		if not type(amount) is int:
			raise TypeError ("The amount must be integer!")
		if amount < 0:
			raise ValueError ("The amount cannot be negative number!")
		self.amount = amount
	def __str__(self):
		return f'A {self.amount}$ bill '
	def __repr__(self):
		return f'A {self.amount}$ bill '
	def __int__(self):
		return int(self.amount)
	def __eq__(self, other):
		return self.amount == other.amount
	def __hash__(self):
		return self.amount
	def __lt__(self, other):
		return self.amount < other.amount

class BatchBill:
	def __init__(self, arr):
		self.arr = arr
	def __len__(self):
		return len(self.arr)
	def total(self):
		sum = 0
		for i in range(len(self.arr)):
			sum +=int(self.arr[i])
		return sum
	def __getitem__(self, index):
		return self.arr[index]
		
class CashDesk:
	def __init__(self):
		self.arg = []
	def __str__(self):
		return ''.join(str(i) for i in self.arg)
	def take_money(self, m):
		if type(m) == Bill:
			self.arg.append(m)
		if type(m) == BatchBill:
			self.arg += m;
	def total(self):
		sum = 0
		for i in self.arg:
			sum += int(i)
		return sum
	def inspect(self):
		dct = {}
		for i in self.arg:
			if i in dct:
				dct[i] += 1
			else:
				dct[i] = 1
		string = ''
		for key in sorted(dct):
			string += str(key) + str(dct[key]) + '\n'
		return string
		

def main():
	b = Bill(4)
	print(int(b))
	print(str(b))
	print(b)
	a2 = Bill(5)
	

	batch = BatchBill([b,a2])
	print(len(batch), batch.total())
	d=CashDesk()
	d.take_money(b)
	d.take_money(batch)
	print(d, d.total())
	dct = d.inspect()
	print(dct)

	for x in batch:
		print(x)

if __name__ == '__main__':
	main()