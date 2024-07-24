from cls.Vector import Vector
import time

class Matrix:
	def __init__(self, matrix) -> None:
		self.matrix = matrix
	
	def print_matrix(self):
		for i in range(len(self.matrix)):
			print(self.matrix[i])

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

	def lerp(self, u: any, v: any, t: float):
		if t == 0:
			return 0.0
		elif t == 1:
			return 1.0
		if isinstance(u, (int, float)) or isinstance(v, (int, float)):
			return Matrix([(v - u) * t + u])
		length = len(u.matrix)
		linear_interpolation = []
		for i in range(length):
			for j in range(len(u.matrix[i])):
				linear_interpolation.append((v.matrix[i][j] - u.matrix[i][j]) * t + u.matrix[i][j])
		return Matrix(linear_interpolation)

	def mul_vec(self, vec):
		length = len(self.matrix)
		if length != vec.size:
			print("Different size!")
			return
		res = []
		for i in range(length):
			temp = []
			for j in range(vec.size):
				temp.append(self.matrix[i][j] * vec.tab[j])
			res.append(sum(temp))
		return Vector(res)

	def mul_mat(self, mat):
		length = len(self.matrix)
		if length != len(mat.matrix):
			print("Different size!")
			return
		res = []
		for i in range(length):
			temp = []
			for j in range(len(mat.matrix)):
				element = 0
				for k in range(len(mat.matrix[0])):
					element += self.matrix[i][k] * mat.matrix[k][j]
				temp.append(element)
			res.append(temp)
		return Matrix(res)

	def trace(self):
		return sum([self.matrix[i][i] for i in range(len(self.matrix))])
	
	def transpose(self):
		return Matrix([[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))])
		
	def row_echelon(self):
		for i in range(len(self.matrix)):
			for j in range(i + 1, len(self.matrix)):
				firstNonNullIndex = 0
				while self.matrix[j][firstNonNullIndex] == 0:
					firstNonNullIndex += 1
				# print(self.matrix[j][firstNonNullIndex])
				while self.matrix[j][firstNonNullIndex] != 0.0:
					scalar = self.matrix[j][firstNonNullIndex] / self.matrix[i][firstNonNullIndex] if self.matrix[i][firstNonNullIndex] != 0.0 else 1.0
					# print(self.matrix[j])
					# time.sleep(1)
					if self.matrix[j][firstNonNullIndex] > 0:
						self.matrix[j] = [a_i - (scalar * b_i) for a_i, b_i in zip(self.matrix[j], self.matrix[i])]
					elif self.matrix[j][firstNonNullIndex] < 0:
						self.matrix[j] = [a_i + (-scalar * b_i) for a_i, b_i in zip(self.matrix[j], self.matrix[i])]
		for k in range(len(self.matrix) - 1, -1, -1):
			firstNonNullIndex = 0
			# print(f"k: {k} {self.matrix[k]}")
			if self.matrix[k] != 0.0:
				break
			while self.matrix[k][firstNonNullIndex] == 0:
				firstNonNullIndex += 1
			self.matrix[k] = [i / self.matrix[k][firstNonNullIndex] + 0.0 for i in self.matrix[k]]
			for l in range(k - 1, -1, -1):
				while self.matrix[l][firstNonNullIndex] != 0.0:
					scalar = self.matrix[l][firstNonNullIndex] / self.matrix[k][firstNonNullIndex]
					if self.matrix[l][firstNonNullIndex] > 0:
						self.matrix[l] = [a_i - (scalar * b_i) for a_i, b_i in zip(self.matrix[l], self.matrix[k])]
					elif self.matrix[l][firstNonNullIndex] < 0:
						self.matrix[l] = [a_i + (-scalar * b_i) for a_i, b_i in zip(self.matrix[l], self.matrix[k])]
		return self

	def __str__(self) -> str:
		return f"{self.matrix}"
