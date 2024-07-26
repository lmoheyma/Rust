import sys

sys.path.append("../")
from cls.Matrix import Matrix

def main():
	u = Matrix([[1.0, 0.0, 0.0],
				[0.0, 1.0, 0.0],
				[0.0, 0.0, 1.0]])
	print(u.rank())

	u = Matrix([[1.0, 2.0, 0.0, 0.0],
				[2.0, 4.0, 0.0, 0.0],
				[-1.0, 2.0, 1.0, 1.0]])
	print(u.rank())

	u = Matrix([[8.0, 5.0, -2.0],
				[4.0, 7.0, 20.0],
				[7.0, 6.0, 1.0],
				[21.0, 18.0, 7.0]])
	print(u.rank())

if __name__ == "__main__":
	main()