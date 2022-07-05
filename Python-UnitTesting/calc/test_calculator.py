import unittest
import calculator

class CalcTest(unittest.TestCase):
  def test_add(self):
    result = calculator.add(10, 7)
    self.assertEqual(result, 17)

if __name__ == '__main__':
  unittest.main()