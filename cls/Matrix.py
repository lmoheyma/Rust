from cls.Vector import Vector
import copy

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
		
	# def row_echelon(self):
	# 	for i in range(len(self.matrix)):
	# 		for j in range(i + 1, len(self.matrix)):
	# 			firstNonNullIndex = 0
	# 			while self.matrix[j][firstNonNullIndex] == 0:
	# 				firstNonNullIndex += 1
	# 			while self.matrix[j][firstNonNullIndex] != 0.0:
	# 				scalar = self.matrix[j][firstNonNullIndex] / self.matrix[i][firstNonNullIndex] if self.matrix[i][firstNonNullIndex] != 0.0 else 1.0
	# 				if self.matrix[j][firstNonNullIndex] > 0:
	# 					self.matrix[j] = [a_i - (scalar * b_i) for a_i, b_i in zip(self.matrix[j], self.matrix[i])]
	# 				elif self.matrix[j][firstNonNullIndex] < 0:
	# 					self.matrix[j] = [a_i + (-scalar * b_i) for a_i, b_i in zip(self.matrix[j], self.matrix[i])]
	# 			print(self.matrix[j])
	# 	for k in range(len(self.matrix) - 1, -1, -1):
	# 		firstNonNullIndex = 0
	# 		if self.matrix[k] == 0.0:
	# 			break
	# 		while self.matrix[k][firstNonNullIndex] == 0:
	# 			firstNonNullIndex += 1
	# 		self.matrix[k] = [i / self.matrix[k][firstNonNullIndex] + 0.0 for i in self.matrix[k]]
	# 		for l in range(k - 1, -1, -1):
	# 			while self.matrix[l][firstNonNullIndex] != 0.0:
	# 				scalar = self.matrix[l][firstNonNullIndex] / self.matrix[k][firstNonNullIndex]
	# 				if self.matrix[l][firstNonNullIndex] > 0:
	# 					self.matrix[l] = [a_i - (scalar * b_i) for a_i, b_i in zip(self.matrix[l], self.matrix[k])]
	# 				elif self.matrix[l][firstNonNullIndex] < 0:
	# 					self.matrix[l] = [a_i + (-scalar * b_i) for a_i, b_i in zip(self.matrix[l], self.matrix[k])]
	# 	return self

	# def row_echelon(self):
	# 	def non_zero_col(self, pivot_row, col):
	# 		nb_rows = len(self.matrix)
	# 		for row in range(pivot_row, nb_rows):
	# 			if self.matrix[row][col] != 0.0:
	# 				return row
	# 		return None
		
	# 	def swap_rows(self, row1, row2):
	# 		self.matrix[row1], self.matrix[row2] = self.matrix[row2], self.matrix[row1]
		
	# 	def reduce_to_pivot_one(self, pivot_row, col):
	# 		pivot = self.matrix[pivot_row][col]
	# 		self.matrix[pivot_row] = [self.matrix[pivot_row][i] // pivot for i in range(len(self.matrix[pivot_row]))]
	# 		print(f"pivot row: {self.matrix[pivot_row]}")

	# 	def zero_below_pivot(self, pivot_row, col):
	# 		nb_rows = len(self.matrix)
	# 		pivot = self.matrix[pivot_row][col]
	# 		for row in range(pivot_row + 1, nb_rows):
	# 			scalar = self.matrix[row][col]
	# 			# print(scalar)
	# 			# self.matrix[row] -= scalar * self.matrix[pivot_row]
	# 			self.matrix[row] = [a_i - (scalar * b_i) for a_i, b_i in zip(self.matrix[row], self.matrix[pivot_row])]

	# 	nb_rows = len(self.matrix)
	# 	nb_cols = len(self.matrix[0])
	# 	# print(nb_cols)
	# 	pivot_row = 0
	# 	for col in range(nb_cols):
	# 		non_zero_row = non_zero_col(self, pivot_row, col)
	# 		if non_zero_row is not None:
	# 			# print("here")
	# 			swap_rows(self, pivot_row, non_zero_row)
	# 			print(non_zero_row)
	# 			print(f"col: {col}")
	# 			reduce_to_pivot_one(self, pivot_row, col)
	# 			zero_below_pivot(self, pivot_row, col)
	# 			pivot_row += 1
	# 	return self

	def row_echelon(self):
		pivot = 0
		self.sign = 1
		nb_rows = len(self.matrix)
		nb_cols = len(self.matrix[0])
		for row in range(nb_rows):
			if pivot >= nb_cols:
				return
			i = row
			while self.matrix[i][pivot] == 0:
				i += 1
				if i == nb_rows:
					i = row
					pivot += 1
					if nb_cols == pivot:
						return
			self.matrix[i], self.matrix[row] = self.matrix[row], self.matrix[i]
			lv = self.matrix[row][pivot]
			self.matrix[row] = [mrx / float(lv) for mrx in self.matrix[row]]
			for i in range(nb_rows):
				if i != row:
					lv = self.matrix[i][pivot]
					self.matrix[i] = [iv - lv * rv for rv, iv in zip(self.matrix[row], self.matrix[i])]
			pivot += 1
		return self

	def determinant(self):
		def is_square(self):
			return len(self.matrix) == len(self.matrix[0])
		
		def determinant_2(matrix: list):
			return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

		def determinant_3(matrix: list):
			det = 0
			for i in range(len(matrix[0])):
				temp = copy.deepcopy(matrix)
				first_coef = temp[0][i]
				for j in temp:
					del j[i]
				coef = determinant_2(temp[1::]) * first_coef
				sign = 1 if i % 2 == 0 else -1
				det += coef * sign
			return det
		
		def determinant_4(matrix):
			det = 0
			for i in range(len(matrix[0])):
				temp = copy.deepcopy(matrix)
				first_coef = temp[0][i]
				for j in temp:
					del j[i]
				coef = determinant_3(temp[1::]) * first_coef
				sign = 1 if i % 2 == 0 else -1
				det += coef * sign
			return det
		if not is_square(self):
			print("Not a square matrix!")
			return
		match len(self.matrix):
			case 2:
				return determinant_2(self.matrix)
			case 3:
				return determinant_3(self.matrix)
			case 4:
				return determinant_4(self.matrix)
			case _:
				print("Matrix too large!")
				return

	def __str__(self) -> str:
		return f"{self.matrix}"
