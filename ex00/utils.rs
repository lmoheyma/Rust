use std::ops::{AddAssign, SubAssign, MulAssign};

pub struct Vector<K> {
	x: K,
	y: K,
}

// struct Matrix::<K> {
// 	//var
// }


impl<K> Vector<K>
where
	K: AddAssign + SubAssign + MulAssign + Copy,	
{
	pub fn from(arr: [K; 2]) -> Self {
        Vector { x: arr[0], y: arr[1] }
    }

	pub fn add(&mut self, v: &Vector<K>) {
		self.x += v.x;
		self.y += v.y;
	}

	// fn sub(&mut self, v: &Vector<K>) {

	// }

	// fn scl(&mut self, a: K) {

	// }
}

// impl<K> Matrix<K> {
// 	fn add(&mut self, v: &Matrix<K>) {
		
// 	}

// 	fn sub(&mut self, v: &Matrix<K>) {
		
// 	}

// 	fn scl(&mut self, a: K) {

// 	}
// }