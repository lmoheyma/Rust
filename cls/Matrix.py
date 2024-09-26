from cls.Vector import Vector
import copy

class Matrix:
	def __init__(self, matrix) -> None:
		self.matrix = matrix
	
	def print_matrix(self):
		for i in range(len(self.matrix)):
			print(self.matrix[i])

	def is_square(self):
		return len(self.matrix) == len(self.matrix[0])

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
			temp = []
			for j in range(len(u.matrix[i])):
				temp.append((v.matrix[i][j] - u.matrix[i][j]) * t + u.matrix[i][j])
			linear_interpolation.append(temp)
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

	def determinant_2(self, matrix: list):
		return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

	def determinant_3(self, matrix: list, row: int):
		det = 0
		for i in range(len(matrix[0])):
			temp = copy.deepcopy(matrix)
			first_coef = temp[row][i]
			for j in temp:
				del j[i]
			del temp[row]
			coef = self.determinant_2(temp) * first_coef
			sign = 1 if i % 2 == 0 else -1
			det += coef * sign
		return det

	def determinant_4(self, matrix: list, row : int):
		det = 0
		for i in range(len(matrix[0])):
			temp = copy.deepcopy(matrix)
			first_coef = temp[row][i]
			for j in temp:
				del j[i]
			del temp[row]
			coef = self.determinant_3(temp, row) * first_coef
			sign = 1 if i % 2 == 0 else -1
			det += coef * sign
		return det

	def determinant(self):	
		if not self.is_square():
			print("Not a square matrix!")
			return
		match len(self.matrix):
			case 2:
				return self.determinant_2(self.matrix)
			case 3:
				return self.determinant_3(self.matrix, 0)
			case 4:
				return self.determinant_4(self.matrix, 0)
			case _:
				print("Matrix too large!")
				return

	def inverse(self):
		def inverse_2(self):
			def cofactor_2(matrix):
				return Matrix([[matrix[0][0], -matrix[0][1]], [-matrix[1][0], matrix[1][1]]])
			cofactor_matrix = cofactor_2(self.matrix)
			transposed_matrix = cofactor_matrix.transpose()
			return Matrix([[(1 / det) * transposed_matrix.matrix[i][j] for j in range(len(transposed_matrix.matrix))] for i in range(len(transposed_matrix.matrix[0]))])
		
		def inverse_3(self, det: float):	
			def cofactor_3(matrix):
				cofactor_matrix = []
				for i in range(len(matrix)):
					cofactor_row = []
					for j in range(len(matrix[i])):
						temp = copy.deepcopy(matrix)
						for k in temp:
							del k[j]
						del temp[i]
						coef = self.determinant_2(temp) * ((-1) ** ((i + 1) + (j + 1))) + 0.0
						cofactor_row.append(coef)
					cofactor_matrix.append(cofactor_row)
				return Matrix(cofactor_matrix)
			cofactor_matrix = cofactor_3(self.matrix)
			transposed_matrix = cofactor_matrix.transpose()
			return Matrix([[(1 / det) * transposed_matrix.matrix[i][j] for j in range(len(transposed_matrix.matrix))] for i in range(len(transposed_matrix.matrix[0]))])

		def inverse_4(self, det: float):
			def cofactor_4(matrix):
				cofactor_matrix = []
				for i in range(len(matrix)):
					cofactor_row = []
					for j in range(len(matrix[i])):
						temp = copy.deepcopy(matrix)
						for k in temp:
							del k[j]
						del temp[i]
						row = i if i < len(temp) else len(temp) - 1
						coef = self.determinant_3(temp, row) * ((-1) ** ((i + 1) + (j + 1))) + 0.0
						cofactor_row.append(coef)
					cofactor_matrix.append(cofactor_row)
				return Matrix(cofactor_matrix)
			cofactor_matrix = cofactor_4(self.matrix)
			transposed_matrix = cofactor_matrix.transpose()
			return Matrix([[(1 / det) * transposed_matrix.matrix[i][j] for j in range(len(transposed_matrix.matrix))] for i in range(len(transposed_matrix.matrix[0]))])
		det = self.determinant()
		if det == 0:
			print("Determinant = 0, can't inverse matrix!")
			return
		if not self.is_square():
			print("Not a square matrix!")
			return
		length = len(self.matrix)
		match length:
			case 2:
				return inverse_2(self)
			case 3:
				return inverse_3(self, det)
			case 4:
				return inverse_4(self, det)
			case _:
				print("Matrix too large!")
				return
		
	def rank(self) -> float:
		self.row_echelon()
		return len(list(filter(lambda x: any(val != 0 for val in x), self.matrix)))
	
	def __str__(self) -> str:
		rows = [f"[{', '.join(map(str, row))}]"for row in self.matrix]
		return '\n'.join(rows) + '\n'
