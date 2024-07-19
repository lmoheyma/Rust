import sys

sys.path.append("../")
from cls.Vector import Vector
from cls.Matrix import Matrix

def main():
	# print(lerp(0.0, 1.0, 0.0))
	# print(lerp(0.0, 1.0, 1.0))
	# print(lerp(0.0, 1.0, 0.5))
	# print(lerp(21.0, 42.0, 0.3))
	u = Vector([2.0, 1.0])
	print(u.lerp(Vector([4.0, 2.0]), 0.3))

	m = Matrix([[2.0, 1.0], [3.0, 4.0]])
	print(m.lerp(Matrix([[20.0, 10.0], [30.0, 40.0]]), 0.5))

if __name__ == "__main__":
	main()