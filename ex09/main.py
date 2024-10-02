import sys

sys.path.append("../")
from cls.Matrix import Matrix

def main():
	u = Matrix([[1.0, 2.0],
			 	[3.0, 4.0]])
	print(u.transpose())

	u = Matrix([[2.0, -5.0, 0.0],
				[4.0, 3.0, 7.0],
				[-2.0, 3.0, 4.0]])
	print(u.transpose())

	u = Matrix([[-2.0, -8.0, 4.0],
				[1.0, -23.0, 4.0]])
	print(u.transpose())

if __name__ == "__main__":
	main() 