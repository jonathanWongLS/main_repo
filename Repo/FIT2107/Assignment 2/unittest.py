import unittest
from unittest.mock import mock
from calculator import Calculator

class CalculatorTest(unittest.TestCase):
    def test_get_solar_insolation(self):
        mockCalculator = mock()
        
        dates = "03/03/2020"
        correct_si = "6.2"

        self.assertEqual(Calculator.get_solar_insolation(mockCalculator, dates), correct_si) 

def main():
    # Create the test suite from the cases above.
    suite = unittest.TestLoader().loadTestsFromTestCase(CalculatorTest)
    # This will run the test suite.
    unittest.TextTestRunner(verbosity=2).run(suite)

main()
        





