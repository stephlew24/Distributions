# Add the Gaussian Module to the system path and import the package to test
sys.path.insert(0, os.path.normpath(os.getcwd() + os.sep + os.pardir))

import sys
import unittest
import datetime
import os
import General_Distribution as d

# Code for the unittest class
class TestDistributionClass(unittest.TestCase):
    def setUp(self) -> None:
        self.distribution = d.Distribution(25, 2)

    def test_initialization(self) -> None:
        self.assertEqual(self.distribution.mean, 25, 'incorrect mean')
        self.assertEqual(self.distribution.stdev, 2, 'incorrct standard deviation')

    def test_read_data_file(self) -> None:
        self.distribution.read_data_file('numbers_gaussian.txt')
        self.assertEqual(len(self.distribution.data), 11, 'data did not load correctly')
        self.distribution.read_data_file('numbers_binomial.txt')
        self.assertEqual(len(self.distribution.data), 13, 'data did not load correctly')

# Run the test
if __name__ == "__main__":
    
    tests = TestDistributionClass()

    tests_loaded = unittest.TestLoader().loadTestsFromModule(tests)
    result = unittest.TextTestRunner().run(tests_loaded)
    result = ", ".join(str(result).split()[1:]).replace(">","")

    # Add to the log file
    filepath = os.path.join('../logs/', 'log_file.txt')
    new_line = '\n'
    with open(filepath, 'a') as f:
        f.write(f'Distribution - {str(datetime.datetime.now())}, {result}{new_line}')
        f.close()
