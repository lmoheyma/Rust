import sys
sys.path.append('../')
from cls.Vector import Vector
from cls.Matrix import Matrix

def main():
	# Addition Vectors
	u = Vector([2.0, 3.0])
	v = Vector([5.0, 7.0])
	u.add(v)
	print(u)

	# Subtract Vectors 
	u = Vector([2.0, 3.0])
	v = Vector([5.0, 7.0])
	u.sub(v)
	print(u)

	# Scaling Vector
	u = Vector([2.0, 3.0])
	u.scl(2.0)
	print(u)

	# Addition Matrix
	u = Matrix([[1.0, 2.0], [3.0, 4.0]])
	v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
	u.add(v)
	print(u)

	# Subtract Matrix
	u = Matrix([[1.0, 2.0], [3.0, 4.0]])
	v = Matrix([[7.0, 4.0], [-2.0, 2.0]])
	u.sub(v)
	print(u)

	# Scaling Matrix
	u = Matrix([[1.0, 2.0], [3.0, 4.0]])
	u.scl(2.0)
	print(u)

if __name__ == "__main__":
	main()
