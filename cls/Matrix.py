class Matrix:
	def __init__(self, matrix) -> None:
		self.matrix = matrix
	
	def add(self, m):
		if len(self.matrix) != len(m.matrix):
			print("Different matrix size!")
			return
		for row in range(len(self.matrix)):
			if (len(self.matrix[row]) != len(self.matrix[0])):
				print("Different matrix size!")
				return
			for column in range(len(self.matrix[0])):
				self.matrix[row][column] += m.matrix[row][column]
	
	def sub(self, m):
		if len(self.matrix) != len(m.matrix):
			print("Different matrix size!")
			return
		for row in range(len(self.matrix)):
			if (len(self.matrix[row]) != len(self.matrix[0])):
				print("Different matrix size!")
				return
			for column in range(len(self.matrix[0])):
				self.matrix[row][column] -= m.matrix[row][column]

	def scl(self, scalar):
		if not isinstance(scalar, (int, float)):
			print("Type Error, scalar must be an int or a float!")
			return
		for row in range(len(self.matrix)):
			for column in range(len(self.matrix[0])):
				self.matrix[row][column] *= scalar

	def lerp(self, v: any, t: float):
		if t == 0:
			return 0.0
		elif t == 1:
			return 1.0
		length = len(self.matrix)
		linear_interpolation = []
		for i in range(length):
			for j in range(len(self.matrix[i])):
				linear_interpolation.append((v.matrix[i][j] - self.matrix[i][j]) * t + self.matrix[i][j])
		return linear_interpolation

	def __str__(self) -> str:
		return f"{self.matrix}"