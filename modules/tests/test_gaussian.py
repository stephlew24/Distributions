# Add the Gaussian Module to the system path and import the package to test
sys.path.insert(0, os.path.normpath(os.getcwd() + os.sep + os.pardir))

import sys
import unittest
import datetime
import os
import math
import Gaussian_Distribution as g

# Code for the unittest class
class TestGaussianClass(unittest.TestCase):
    def setUp(self) -> None:
        self.gaussian = g.Gaussian(25, 2)

    def test_initialization(self) -> None:
        self.assertIsInstance(self.gaussian.mean, float, 'incorrect mean')
        self.assertIsInstance(self.gaussian.stdev, float, 'incorrect standard deviation')
    
    def test_analyzedataset(self) -> None:
        self.gaussian.read_data_file('numbers_gaussian.txt')
        self.gaussian.analyze_data_set(True)
        self.assertEqual(round(self.gaussian.mean, 2), 78.09, 'incorrect mean')
        self.assertEqual(round(self.gaussian.stdev, 2), 92.87, 'incorrect standard deviation')
        self.assertEqual(round(self.gaussian.n, 2), 11, 'incorrect number of observations')

        self.gaussian.read_data_file('numbers_gaussian.txt')
        with self.assertRaises(ValueError) as exception_context:
            self.gaussian.analyze_data_set(False)
        self.assertEqual(str(exception_context.exception), "Could not estimate the parameters of this data set. N (11) must be >= 20")
        self.assertEqual(round(self.gaussian.mean, 2), 78.09, 'incorrect mean')
        self.assertEqual(round(self.gaussian.stdev, 2), 88.55, 'incorrect standard deviation')
        self.assertEqual(round(self.gaussian.n, 2), 11, 'incorrect number of observations')

    def test_meancalculation(self) -> None:
        self.gaussian.read_data_file('numbers_gaussian.txt')
        self.assertEqual(self.gaussian.calculate_mean(True),\
            (sum(self.gaussian.data) / float(len(self.gaussian.data))), 'sample mean not as expected')

        # Test the estimated population mean
        self.gaussian.read_data_file('numbers_gaussian.txt')
        with self.assertRaises(ValueError) as exception_context:
            self.gaussian.analyze_data_set(False)
        self.assertEqual(str(exception_context.exception), "Could not estimate the parameters of this data set. N (11) must be >= 20")

        # Test the estimated population mean calculation
        gaussian = self.gaussian = g.Gaussian(5, 1, 1000)
        self.gaussian.analyze_data_set(False)
        # self.assertEqual() # Calculate it manually if possible
    
    def test_stdevcalculation(self) -> None:
        self.gaussian.read_data_file('numbers_gaussian.txt')
        self.gaussian.analyze_data_set(True)
        self.assertEqual(self.gaussian.calculate_stdev(True), math.sqrt(sum([(x -\
            (sum(self.gaussian.data) / float(len(self.gaussian.data)))) ** 2 for x in self.gaussian.data])\
                / (len(self.gaussian.data)-1)), 'sample standard deviation incorrect')
        self.gaussian.read_data_file('numbers_gaussian.txt')
        with self.assertRaises(ValueError) as exception_context:
            self.gaussian.analyze_data_set(False)
        self.assertEqual(str(exception_context.exception), "Could not estimate the parameters of this data set. N (11) must be >= 20")
    
    def test_pdf(self) -> None:
        self.assertIsInstance(self.gaussian.pdf(25), float, 'pdf function does not give expected result')
    
    def test_plothistogrampdf(self) -> None:
        self.gaussian.read_data_file('numbers_gaussian.txt')
        self.gaussian.analyze_data_set(True)
        self.assertEqual(self.gaussian.plot_histogram_pdf(5), ([1.0, 66.8, 132.6, 198.39999999999998, 264.2],\
        [0.0030436941280150395, 0.004263868097796145, 0.003615877323227138, 0.0018562257166269047, 0.0005768395828224327]),\
        'x and y are incorrect')
        self.gaussian.read_data_file('numbers_gaussian.txt')
        with self.assertRaises(ValueError) as exception_context:
            self.gaussian.analyze_data_set(False)
        self.assertEqual(str(exception_context.exception), "Could not estimate the parameters of this data set. N (11) must be >= 20")

# Run the test
if __name__ == "__main__":
    
    tests = TestGaussianClass()

    tests_loaded = unittest.TestLoader().loadTestsFromModule(tests)

    result = unittest.TextTestRunner().run(tests_loaded)
    result = ", ".join(str(result).split()[1:]).replace(">","")

    # Add to the log file
    filepath = os.path.join('../logs/', 'log_file.txt')
    new_line = '\n'
    with open(filepath, 'a') as f:
        f.write(f'Gaussian - {str(datetime.datetime.now())}, {result}{new_line}')
        f.close()
