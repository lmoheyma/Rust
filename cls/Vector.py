class Vector:
	def __init__(self, tab) -> None:
		self.tab = tab
		self.size = len(tab)
	
	def add(self, v):
		if self.size != v.size:
			print("Different vector size!")
			return
		for value in range(self.size):
			self.tab[value] += v.tab[value]
	
	def sub(self, v):
		if self.size != v.size:
			print("Different vector size!")
			return
		for value in range(self.size):
			self.tab[value] -= v.tab[value]

	def scl(self, scalar):
		if not isinstance(scalar, (int, float)):
			print("Type Error, scalar must be an int or a float!")
			return
		for value in range(self.size):
			self.tab[value] *= scalar

	def __str__(self) -> str:
		return f"{self.tab}"