import calculatorv2
import unittest


class TestCalculator(unittest.TestCase):
    def test_Add(self):
        self.assertEqual(calculatorv2.add(1,1),2)
        with self.assertRaises(TypeError):
             calculatorv2.add('1',1)
    
#    def test_DivideByZero(self):
      #  self.assertFalse(calculatorv2.divide(1,0))
        #with assertRaises(ZeroDivisionError):
         #   pass
      #  self.assertRaises(ZeroDivisionError, calculatorv2.divide(1,0),None)
     #   with self.assertRaises(ZeroDivisionError):
     #       calculatorv2.divide(1,0) 
       # with self.assertRaises(ZeroDivisionError):
       #      calculatorv2.divide(1,0)
   
    def test_Subtract(self):
        self.assertEqual(calculatorv2.subtract(1,1),0)

    def test_Multiply(self):
        self.assertEqual(calculatorv2.multiply(1,1),1)

    def test_Divide(self):
        self.assertEqual(calculatorv2.divide(1,1),1)
        with self.assertRaises(ZeroDivisionError):
            calculatorv2.divide(10,0)
    def test_operator(self):
        self.assertEqual(calculatorv2.operator('+',13,11),24)
        self.assertEqual(calculatorv2.operator('-',15,-10),25)
        self.assertEqual(calculatorv2.operator('/',16,2),8)
        self.assertEqual(calculatorv2.operator('*',7,-3),-21)
        self.assertEqual(calculatorv2.operator(1,'AB', 3), None)

    def test_output(self):
        self.assertEqual(calculatorv2.output('+',13,11,24),'13 + 11 = 24')

    def test_op(self):
        self.assertEqual(calculatorv2.input_operator(self.mock_op),'+')

    def test_inputOne(self):
        self.assertEqual(calculatorv2.inputOne(self.mock_input), 1)

    def test_inputTwo(self):
        self.assertEqual(calculatorv2.inputTwo(self.mock_input),1)

    def mock_input(self,prompt):
        return 1
    def mock_op(self,prompt):
        return '+'

    def test_success(self):
        num1 = calculatorv2.inputOne(self.mock_input)
        op = calculatorv2.input_operator(self.mock_op)
        num2 = calculatorv2.inputTwo(self.mock_input)
        ans = calculatorv2.operator(op,num1,num2)
        final = calculatorv2.output(op,num1,num2,ans)
        self.assertEqual(final, '1 + 1 = 2')



if __name__ == '__main__':
    unittest.main()
