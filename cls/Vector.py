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

	def linear_combination(_self, u: list, coefs: list):
		if len(u) != len(coefs):
			print("Different size!")
			return
		combination = []
		element = 0
		for i in range(len(u)):
			for j in range(len(u[i].tab)):
				element += u[i].tab[j] * coefs[i]
			combination.append(element)
			element = 0
		return Vector(combination)

	def lerp(self, v: any, t: float):
		if t == 0:
			return 0.0
		elif t == 1:
			return 1.0
		length = len(self.tab)
		linear_interpolation = []
		for i in range(length):
			linear_interpolation.append((v.tab[i] - self.tab[i]) * t + self.tab[i])
		return Vector(linear_interpolation)

	def __str__(self) -> str:
		return f"{self.tab}"