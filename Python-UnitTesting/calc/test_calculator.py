import unittest
import calculator

class CalcTest(unittest.TestCase):
  '''
  make sure with keyword `test_` 
    e.g.  test_add (√)
          add_test (x) - not running test

  '''
  def test_add(self):   
    self.assertEqual(calculator.add(10, 7), 17)
    self.assertEqual(calculator.add(-1, 10), 9)
    self.assertEqual(calculator.add(2, 4), 6)

  def test_substract(self):   
    self.assertEqual(calculator.substract(10, 7), 3)
    self.assertEqual(calculator.substract(-1, -1), 0)
    self.assertEqual(calculator.substract(2, 4), -2)

  def test_multiply(self):   
    self.assertEqual(calculator.multiply(10, 7), 70)
    self.assertEqual(calculator.multiply(-1, 10), -10)
    self.assertEqual(calculator.multiply(2, 4), 8)

  def test_division(self):   
    self.assertEqual(calculator.division(10, 2), 5)
    self.assertEqual(calculator.division(4, 2), 2)
    self.assertEqual(calculator.division(5, 2), 2.5)
    # self.assertRaises(ValueError, calculator.division, 10, 0) 
    with self.assertRaises(ValueError):   # alternative
      calculator.division(10, 0)

if __name__ == '__main__':
  unittest.main()