import superFizzBuzz
import unittest
class testCountCamelCase(unittest.TestCase):
    def test_give_225_should_be_FizzFizzBuzzBuzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(225),"FizzFizzBuzzBuzz",'output should be FizzFizzBuzzBuzz')
    def test_give_450_should_be_FizzFizzBuzzBuzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(450),"FizzFizzBuzzBuzz",'output should be FizzFizzBuzzBuzz')
    def test_give_675_should_be_FizzFizzBuzzBuzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(675),"FizzFizzBuzzBuzz",'output should be FizzFizzBuzzBuzz')

    def test_give_15_should_be_FizzBuzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(15),"FizzBuzz",'output should be FizzBuzz')
    def test_give_30_should_be_FizzBuzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(30),"FizzBuzz",'output should be FizzBuzz')
    def test_give_45_should_be_FizzBuzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(45),"FizzBuzz",'output should be FizzBuzz')

    def test_give_9_should_be_FizzFizz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(9),"FizzFizz",'output should be FizzFizz')
    def test_give_18_should_be_FizzFizz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(18),"FizzFizz",'output should be FizzFizz')
    def test_give_27_should_be_FizzFizz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(27),"FizzFizz",'output should be FizzFizz')

    def test_give_25_should_be_BuzzBuzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(25),"BuzzBuzz",'output should be BuzzBuzz')
    def test_give_50_should_be_BuzzBuzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(50),"BuzzBuzz",'output should be BuzzBuzz')
    def test_give_100_should_be_BuzzBuzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(100),"BuzzBuzz",'output should be BuzzBuzz')

    def test_give_3_should_be_Fizz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(3),"Fizz",'output should be Fizz')
    def test_give_6_should_be_Fizz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(6),"Fizz",'output should be Fizz')
    def test_give_21_should_be_Fizz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(21),"Fizz",'output should be Fizz')

    def test_give_5_should_be_Buzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(5),"Buzz",'output should be Buzz')
    def test_give_20_should_be_Buzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(20),"Buzz",'output should be Buzz')
    def test_give_40_should_be_Buzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(40),"Buzz",'output should be Buzz')

    def test_give_1_should_be_NoFizzBuzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(1),"NoFizzBuzz",'output should be NoFizzBuzz')
    def test_give_14_should_be_NoFizzBuzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(14),"NoFizzBuzz",'output should be NoFizzBuzz')
    def test_give_37_should_be_NoFizzBuzz(self):
        self.assertEqual(superFizzBuzz.superFizzBuzzFunction(37),"NoFizzBuzz",'output should be NoFizzBuzz')

