import sys

sys.path.append("../")
from cls.Vector import Vector
from cls.Matrix import Matrix

def main():
	u = Vector([0.0, 0.0])
	v = Vector([1.0, 1.0])
	print(u.dot(v))

	u = Vector([1.0, 1.0])
	v = Vector([1.0, 1.0])
	print(u.dot(v))

	u = Vector([-1.0, 6.0])
	v = Vector([3.0, 2.0])
	print(u.dot(v))

if __name__ == "__main__":
	main()