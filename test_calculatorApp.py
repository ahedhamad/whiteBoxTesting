import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp

class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")
        self.patcher1 = patch('calculatorApp.add', return_value = 5)
        self.MockClass1 = self.patcher1.start()
        self.addCleanup(self.patcher1.stop)
##function add
    def test_AddPass(self):
        self.assertEqual(add(6,3), 9)# will execute the add
        self.assertEqual(calculate('1',6,3), 5) # will call the mock
    ##function sub
    def test_subPass(self):
        self.assertEqual(subtract(5,2), 3)# will execute the sub
        self.assertEqual(calculate('2',5,2), 3) # will call the mock
##function multi
    def test_multiPass(self):
        self.assertEqual(multiply(3,2), 6)# will execute the multi
        self.assertEqual(calculate('3',3,2),(3,'*',2,'=',6)) # will call the mock
##function divide 
    def test_dividePass(self):
        self.assertEqual(divide(6,2), 3)# will execute the divid
        self.assertEqual(calculate('4',6,2),(6,'/',2,'=',3)) # will call the mock
     ## when number 1 = 0
    def test_dividePassZero(self):
        with self.assertRaises(ValueError):
             self.assertEqual(divide(0,2), 0)# will execute the divid
             self.assertEqual(calculate('4',0,2),(0,'/',2,'=',0))    
##function divide By Zero
    def test_DividByZeroEX1(self):
         with self.assertRaises(ZeroDivisionError):
              divide(7,0)
              calculate('4','7','0')

    def test_PrintDivideByZerro(self):     
        with self.assertRaises(ZeroDivisionError) as exception_context:
             calculate('4',2,'0')
             self.assertEqual(str(exception_context.exception),"You can't divide by zero!")

## function check user input
    def test_checkEmpty(self):     
        with self.assertRaises(ValueError) as exception_context:
             check_user_input("")
             self.assertEqual(str(exception_context.exception),"Input can't be empty")# will execute the divid  
       ## check string 
    def test_check_user_inputString(self):
        with self.assertRaises(ValueError):
             check_user_input('Hrr')
        ## check symbole      
    def test_check_user_inputSymbol(self):
        with self.assertRaises(Exception):
             check_user_input('@')

    def test_check_user_inputNumber(self):
         self.assertEqual(check_user_input('1') ,1)  

    def test_test(self):
        self.assertIsInstance(check_user_input('5.6'), float)    
    ##function calculator

    def test_AddInvalid(self):
        self.assertNotEqual(calculate('1',9,3), 9)

    def test_subInvalid(self):
        self.assertNotEqual(calculate('2',8,6), 3)

    def test_multiInvalid(self):
        self.assertNotEqual(calculate('3',7,2), 16)    
   
    def test_DividByZerrorEx1(self):
        with self.assertRaises(ValueError):
             calculate('4','3','w')

    def test_InvalidNumber(self):
        with self.assertRaises(ValueError):
             calculate('1',' ', 1)

    def test_Invalidchoise(self):
        with self.assertRaises(Exception):
             calculate('5',2, 1)

## function is Exit
    def test_isExit_N(self):
        self.assertNotEqual(isExit("no"), "no")

    def test_isExit_Y(self):
        self.assertNotEqual(isExit("yes"), "yes")

    def test_isExit_YN(self):
        with self.assertRaises(ValueError):
            isExit('1')

    ##OR

    def test_DividByZerrorEx2(self):
        self.assertRaises(ValueError, calculate, '4','3','w')

    def test_DividByZerrorRegex(self):
        with self.assertRaisesRegex(ValueError, "input is not a number!"):
             calculate('4','3','w')

   
    def test_AddPassWithMockEx1(self):
        with mock.patch('calculatorApp.add', return_value = 6):
            result = calculate('1',2,4)
        self.assertEqual(result, 6)

    @mock.patch('calculatorApp.add', return_value = 4)
    def test_AddPassWithMockEx2(self, mock_check):
        result = calculate('1',3,2)
        self.assertEqual(result, 4)


    def test_AddPassWithMocEx3(self):
        assert calculatorApp.add is self.MockClass1
        self.assertEqual(calculate('1',2,6), 5)
       
   

    def tearDown(self):
        print("tearDown .. ")
        #self.patcher1.stop()#or add this and remove self.addCleanup(self.patcher1.stop) in startup but this is not recommened!


class TestCalculateWithoutMock(unittest.TestCase):
    def test_AddPass(self):
        self.assertEqual(add(6,3), 9)
        self.assertEqual(calculate('1',6,3), 9)

    def test_subPass(self):
        self.assertEqual(subtract(5,2), 3)
        self.assertEqual(calculate('2',5,2), 3)

    def test_multiPass(self):
        self.assertEqual(multiply(3,2), 6)
        self.assertEqual(calculate('3',3,2),(3,'*',2,'=',6))

    def test_dividPass(self):
        self.assertEqual(divide(6,2), 3)
        self.assertEqual(calculate('4',6,2),(6,'/',2,'=',3))


if __name__ == '__main__':
	unittest.main()
