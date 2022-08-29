import unittest
from functions import multiply, even

class MyTest(unittest.TestCase):

	def test_multiply(self):
		self.assertEqual(multiply(2, 3), 6)

	def test_even(self):
		self.assertTrue(even(2))


if __name__ == '__main__':
	unittest.main()