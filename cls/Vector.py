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

	def lerp(self, u: any, v: any, t: float):
		if t == 0:
			return Vector([0.0])
		elif t == 1:
			return Vector([1.0])
		if isinstance(u, (int, float)) or isinstance(v, (int, float)):
			return Vector([(v - u) * t + u])
		length = len(u.tab)
		linear_interpolation = []
		for i in range(length):
			linear_interpolation.append((v.tab[i] - u.tab[i]) * t + u.tab[i])
		return Vector(linear_interpolation)
	
	def dot(self, v) -> float:
		if self.size != v.size:
			print("Different vector size!")
			return
		dot_product = 0.0
		for i in range(self.size):
			dot_product += self.tab[i] * v.tab[i]
		return dot_product
	
	def norm_1(self) -> float:
		norm = sum([i for i in self.tab])
		if norm < 0:
			return -norm
		return norm
	
	def norm(self) -> float:
		return sum([i * i for i in self.tab])**0.5
	
	def norm_inf(self) -> float:
		def abs(nb: float):
			if nb < 0:
				return -nb
			return nb
		return max([abs(i) for i in self.tab])
	
	def angle_cos(self, v: any) -> float:
		if self.size != v.size:
			print("Different vectors size!")
			return
		denominator = self.norm() * v.norm()
		if denominator == 0:
			print("Division by Zero!")
			return
		return (self.dot(v) / denominator)

	def cross_product(self, v):
		if self.size != 3 or v.size != 3:
			print("Wrong vector size!")
			return
		return ([(self.tab[1] * v.tab[2]) - (self.tab[2] * v.tab[1]),
				(self.tab[2] * v.tab[0]) - (self.tab[0] * v.tab[2]),
				(self.tab[0] * v.tab[1]) - (self.tab[1] * v.tab[0])])

	def __str__(self) -> str:
		return f"{self.tab}"
