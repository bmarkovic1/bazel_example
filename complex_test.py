import unittest
from math import sqrt 

from complex import Complex

class Tests(unittest.TestCase):

    def test_constuctor(self):
        c = Complex(1, 2)
        self.assertEqual(1, c.real)
        self.assertEqual(2, c.imag)

    def test_add(self):
        a = Complex(1, 2)
        b = Complex(3, 4)
        c = a + b
        self.assertEqual(1 + 3, c.real)
        self.assertEqual(2 + 4, c.imag)
    
    def test_sub(self):
        a = Complex(1, 2)
        b = Complex(3, 4)
        c = a - b
        self.assertEqual(1 - 3, c.real)
        self.assertEqual(2 - 4, c.imag)

    def test_mul(self):
        a = Complex(1, 2)
        b = Complex(3, 4)
        c = a * b
        self.assertEqual(a.real * b.real - a.imag * b.imag, c.real)
        self.assertEqual(a.real * b.imag + a.imag * b.real, c.imag)

    def test_abs(self):
        a = Complex(1, 2)
        b = abs(a)
        self.assertEqual(sqrt(a.real**2 + a.imag**2), b)

    def test_neg(self):
        a = Complex(1, 2)
        b = -a
        self.assertEqual(a.real, - b.real)
        self.assertEqual(a.imag, - b.imag)

    def test_equal(self):
        a = Complex(1, 2)
        b = Complex(1, 2)
        self.assertEqual(a, b)

    def test_str(self):
        a = Complex(1, 2)
        b = str(a)
        self.assertEqual(type(b), str)


if __name__ == '__main__':
    unittest.main()