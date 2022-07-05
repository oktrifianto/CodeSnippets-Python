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

if __name__ == '__main__':
  unittest.main()