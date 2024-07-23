import sys

sys.path.append("../")
from cls.Vector import Vector

def main():
	u = Vector([1.0, 0.0])
	v = Vector([1.0, 0.0])
	print(u.angle_cos(v))

	u = Vector([1.0, 0.0])
	v = Vector([0.0, 1.0])
	print(u.angle_cos(v))

	u = Vector([-1.0, 1.0])
	v = Vector([1.0, -1.0])
	print(u.angle_cos(v))

	u = Vector([2.0, 1.0])
	v = Vector([4.0, 2.0])
	print(u.angle_cos(v))

	u = Vector([1.0, 2.0, 3.0])
	v = Vector([4.0, 5.0, 6.0])
	print(u.angle_cos(v))

if __name__ == "__main__":
	main()