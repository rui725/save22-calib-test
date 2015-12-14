import calculatorv2
import unittest

class TestCalculator_Bugs(unittest.TestCase):
    def test_DividedByZero(self):
        self.assertRaises(ZeroDivisionError,calculatorv2.divide, 1,0)
    def test_StringInputs(self):
      #  self.assertEquals(calculatorv2.add('A','A'))
      #  with assertRaises(TypeError):
      #       calculatorv2.add('A','A')
        one = self.assertRaises(TypeError,calculatorv2.inputOne,'A')
        two = self.assertRaises(TypeError,calculatorv2.inputTwo, 'A') 
        self.assertRaises(TypeError,calculatorv2.add,one,two)
    def test_IntandString(self):
        one = self.assertRaises(TypeError,calculatorv2.inputOne,1)
        two = self.assertRaises(TypeError,calculatorv2.inputTwo,'A')
        self.assertRaises(TypeError,calculatorv2.add,one,two)


if __name__ == '__main__':
    unittest.main()
