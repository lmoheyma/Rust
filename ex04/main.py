import sys

sys.path.append("../")
from cls.Vector import Vector

def main():
	u = Vector([0.0, 0.0, 0.0])
	print(f"{u.norm_1()}, {u.norm():.8f}, {u.norm_inf()}")

	u = Vector([1.0, 2.0, 3.0])
	print(f"{u.norm_1()}, {u.norm():.8f}, {u.norm_inf()}")

	u = Vector([-1.0, -2.0])
	print(f"{u.norm_1()}, {u.norm():.8f}, {u.norm_inf()}")

if __name__ == "__main__":
	main()