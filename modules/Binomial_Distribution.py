# %%
import os
import math
import matplotlib.pyplot as plt
from scipy.stats import bernoulli, norm
import numpy as np
import General_Distribution as General_Distribution

class Binomial(General_Distribution.Distribution):

    def __init__(self, prob: float = .5, n: int = 25, file_name: str or None = None) -> None:

        if file_name:
            self.data = self.read_data_file(file_name)
            self.n = len(self.data)
            General_Distribution.Distribution.__init__(self)
            self.analyze_data_set()
        else:
            self.n = n
            self.prob = prob
            General_Distribution.Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())

        """ 
            Class to calculate and visualize a Binomial distributions
        
            Attributes:
                mean (float): calculates the mean value of the distribution
                stdev (float): calculates the standard deviation of the distribution
                data (list[float]): a list of floats extracted from the data file
                p (float): calculates the probability of a binary event occuring
                n (int): the number of observations in the data set

        """

    def analyze_data_set(self, sample: bool = False) -> 'float, float, float, int':
        """ 
            Method to populate the variables of the Binomial class based on the loaded data set

            Args:
                sample (bool): flag if sample data approximating the distribution
                should be generated.

            Returns:
                float: the mean of the data set
                float: the standard deviation of the data set
                float: the probability of the positive class in the data set
                int: the number of observations in the data set
        """
        if sample:
            self.data = bernoulli(self.prob).rvs(self.n)

        self.n = len(self.data)    
        self.prob = sum(self.data)/self.n * 1.0
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.mean, self.stdev, self.prob, self.n 

    def calculate_mean(self) -> float:

        """ 
            Method to calculate the mean of the data set.

            Args:
                None
        
            Returns:
                float: mean of the data set.

        """

  
        _mean = (self.prob * self.n) * 1.0

        return _mean

    def calculate_stdev(self) -> float:

        """ 
            Method to calculate the mean of the standard deviation of the data set.

            Args:
                None
        
            Returns:
                float: mean of the data set.

        """

        _n = self.n
    
        _stdev = math.sqrt(_n * self.prob * (1-self.prob))

        return _stdev

    def plot_bar(self) -> None:
        """
            Function to plot a bar graph of the instance variable 
            using the matplotlib pyplot library.

            Args:
                None
            
            Returns:
                None
           
        """
        plt.bar(x=['0','1'], height = [(1 - self.prob) * self.n, self.prob * self.n])
        plt.title('Bar Chart of Outcomes')
        plt.xlabel('Outcome')
        plt.ylabel('Count')
        plt.show()
    
    def pdf(self, x: float) -> float:
        """
            Probability density function calculator for the bionomial distribution.

            Args:
                x (float): point for calculating the probability density function. Must be x =< n
            
            Returns:
                float: probability density function output
        
        """

        # Binomial Formula. Suppose a binomial experiment consists of n trials and results in x successes. 
        # If the probability of success on an individual trial is P, then the binomial probability is:

        # b(x; n, P) = nCx * Px * (1 - P)n - x 
        # OR 
        # b(x; n, P) = { n! / [ x! (n - x)! ] } * Px * (1 - P)n - x
        
        if x <= self.n:
            a = math.factorial(self.n)/ (math.factorial(x) * (math.factorial(self.n - x)))
            b = (self.prob ** x) * (1 - self.prob) ** (self.n - x)
            return a * b
        else:
            raise ValueError("x must be n or less")
    
    def plot_bar_pdf(self, n_spaces: int = 50) -> 'list[float], list[float]':

        """
            Function to plot the normalied histogram of the data and the probability
            density function.

            Args:
                n_spaces (int): number of data points to plot
            
            Returns:
                list[float]: x values for pdf plot
                list[float]: y values for pdf plot

        """
        
        # Calcuate the x values for ploting
        _x = [x for x in range(self.n + 1)]
        _y = [self.pdf(x) for x in _x]

        # Create the plots
        fig, axes = plt.subplots(ncols=1, nrows=2)
        fig.subplots_adjust(hspace=.5)
        axes[0].bar(x=['0','1'], height = [((1 - self.prob) * self.n)/self.n, (self.prob * self.n)/self.n])
        axes[0].set_title('Normalized Bar Chart of Outcomes')
        axes[0].set_ylabel('Count')

        axes[1].plot(_x, _y)
        axes[1].set_title('Distribution of Outcomes')
        axes[1].set_ylabel('Count')
        plt.show()

        return _x, _y

    def __add__(self, other: type) -> type:
        """
            Function to add together two Binomial distributions.

            Args:
                other (Binomial): A instance of the Binomial class.
            
            Returns:
                type (Binomial): Combination of the two Binomial distributions as a Binomial instance.
        
        """
        
        try:
            assert self.prob == other.prob, 'probabilities are not equal'
        except AssertionError as error:
            raise

        result = Binomial()
        result.n = self.n + other.n
        result.prob = self.prob
        result.calculate_mean()
        result.calculate_stdev()

        return result

    def __repr__(self):
        """
            Function to return the characteristics of the Binomial instance.

            Args:
                None
            
            Returns:
                str: characteristics of the Binomial instance.
        
        """

        return f'Mean: {self.mean}, Standard Deviation: {self.stdev}, Probability: {self.prob:.0%}, N: {self.n}' 
