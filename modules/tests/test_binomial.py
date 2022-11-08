# %%
import sys
import unittest
import datetime
import os
import math

# Add the Gaussian Module to the system path and import the package to test
sys.path.insert(0, os.path.normpath(os.getcwd() + os.sep + os.pardir))
import Binomial_Distribution as b

# Code for the unittest class
class TestBinomialClass(unittest.TestCase):
    def setUp(self) -> None:
        self.binomial = b.Binomial(.5, 2)

    def test_initialization(self) -> None:
        self.assertEqual(self.binomial.prob, .5, 'incorrect probability')
        self.assertEqual(self.binomial.n, 2, 'incorrect standard deviation')

    def test_analyzedataset(self) -> None:
        self.binomial.read_data_file('numbers_binomial.txt')
        self.binomial.analyze_data_set(False)
        self.assertEqual(round(self.binomial.mean, 1), 8.0, 'incorrect mean')
        self.assertEqual(round(self.binomial.stdev, 2), 1.75, 'incorrect standard deviation')
        self.assertEqual(round(self.binomial.prob, 2), 0.62, 'incorrect probability')
        self.assertEqual(round(self.binomial.n, 3), 13, 'incorrect number of observations')

        self.binomial.read_data_file('numbers_binomial.txt')
        self.binomial.analyze_data_set(True)
        self.assertNotEqual(round(self.binomial.mean, 1), 8.0, 'incorrect mean')
        self.assertNotEqual(self.binomial.stdev, 1.7541160386140584, 'incorrect standard deviation')
        self.assertNotEqual(self.binomial.prob, 0.6153846153846154, 'incorrect probability')
        self.assertEqual(round(self.binomial.n, 3), 13, 'incorrect number of observations')
    
    def test_meancalculation(self) -> None:
        self.binomial.read_data_file('numbers_binomial.txt')
        self.binomial.analyze_data_set(False)
        self.assertEqual(self.binomial.calculate_mean(),\
            (self.binomial.prob) * len(self.binomial.data), 'mean not as expected')

    def test_stdevcalculation(self) -> None:
        self.binomial.read_data_file('numbers_binomial.txt')
        self.binomial.analyze_data_set(False)
        self.assertEqual(self.binomial.calculate_stdev(),\
            math.sqrt((len(self.binomial.data) * self.binomial.prob * (1-self.binomial.prob))),\
                'standard deviation not as expected')

    def test_pdf(self) -> None:
        self.assertEqual(round(self.binomial.pdf(2), 2), 0.25,\
            'pdf function does not give expected result')

    def test_plotbarpdf(self) -> None:
        self.assertEqual(self.binomial.plot_bar_pdf(2), ([0, 1, 2], [0.25, 0.5, 0.25]),
        'x and y are incorrect')

# Run the test
if __name__ == "__main__":
    
    tests = TestBinomialClass()

    tests_loaded = unittest.TestLoader().loadTestsFromModule(tests)

    result = unittest.TextTestRunner().run(tests_loaded)
    result = ", ".join(str(result).split()[1:]).replace(">","")

    # Add to the log file
    filepath = os.path.join('../logs/', 'log_file.txt')
    new_line = '\n'
    with open(filepath, 'a') as f:
        f.write(f'Binomial - {str(datetime.datetime.now())}, {result}{new_line}')
        f.close()