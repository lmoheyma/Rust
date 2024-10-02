import sys

sys.path.append("../")
from cls.Vector import Vector
from cls.Matrix import Matrix

def main():
	tmpVector = Vector([0])
	tmpMatrix = Matrix([0])

	print(tmpVector.lerp(0.0, 1.0, 0.0))
	print(tmpVector.lerp(0.0, 1.0, 1.0))
	print(tmpVector.lerp(0.0, 1.0, 0.5))
	print(tmpVector.lerp(21.0, 42.0, 0.3))

	print(tmpVector.lerp(Vector([2.0, 1.0]), Vector([4.0, 2.0]), 0.3))

	print(tmpMatrix.lerp(Matrix([[2.0, 1.0], [3.0, 4.0]]), Matrix([[20.0, 10.0], [30.0, 40.0]]), 0.5))

if __name__ == "__main__":
	main()
