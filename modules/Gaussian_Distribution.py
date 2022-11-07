# %%
import os
import math
import matplotlib.pyplot as plt
import General_Distribution as General_Distribution

# %%

class Gaussian(General_Distribution.Distribution):

    def __init__(self, mean: float = 0, stdev: float = 0, file_name: str or None = None) -> None:
        
        if file_name:
            self.data = self.read_data_file(file_name)
            self.n = len(self.data)
            General_Distribution.Distribution.__init__(self, self.calculate_mean(False), self.calculate_stdev(False))
        else:
            General_Distribution.Distribution.__init__(self, mean, stdev)
        
        """ 
            Class to calculate and visualize a Gaussian distributions
        
            Attributes:
                mean (float) calculates the mean value of the distribution
                stdev (float) calculates the standard deviation of the distribution
                data (list[float]) a list of floats extracted from the data file
                n (int) number of observations in the data set

        """

    def analyze_data_set(self, sample: bool = True) -> 'float, float, int':
        """ 
            Method to populate the variables of the Gaussian class based on the loaded data set

            Args:
                None

            Returns:
                float: the mean of the data set
                float: the standard deviation of the data set
                int: the number of observations in the dataset

        """
        if self.data:
            self.n = len(self.data)
            self.mean = self.calculate_mean(sample)
            self.stdev = self.calculate_stdev(sample)
        else:
            print('Please load the data using the ".read_data_file()" method')
        
        return self.mean, self.stdev#, self.n

    def calculate_mean(self, sample: bool = True) -> float:

        """ 
            Method to calculate the mean of the data set.

            Args:
                sample (bool): flag whether the data represents the sample 
                or population.
        
            Returns:
                float: mean of the data set.

        """

        if sample:
            _mean = sum(self.data)/len(self.data) * 1.0
        else:
            # Estimate the population mean
            _mean = sum(self.data)/len(self.data) * 1.0
            # pass

        return _mean

    def calculate_stdev(self, sample: bool = True) -> float:

        """ 
            Method to calculate the mean of the standard deviation of the data set.

            Args:
                sample (bool): flag whether the data represents the sample or population.
        
            Returns:
                float: mean of the data set.

        """

        if sample:
            n = self.n - 1            
        else:
            n = self.n

        _mean = self.calculate_mean(sample)
        
        stdev = math.sqrt(sum([(x - _mean) ** 2 for x in self.data]) / n)
     
        return stdev      
    
    def plot_histogram(self) -> None:
        """
            Function to plot a histogram of the instance variable 
            using the matplotlib pyplot library.

            Args:
                None
            
            Returns:
                None
           
        """
        plt.hist(self.data)
        plt.title("Histogram")
        plt.xlabel('data')
        plt.ylabel('count')
        plt.show()
    
    def pdf(self, x: float) -> float:
        """
            Probability density function calculator for the gaussian distribution.

            Args:
                x (float): point for calculating the probability density function.
            
            Returns:
                float: probability density function output
        
        """

        return (1.0 / (self.stdev * math.sqrt(2*math.pi))) * math.exp(-0.5*((x - self.mean) / self.stdev) ** 2)
    
    def plot_histogram_pdf(self, n_spaces: int = 50) -> "list[float], list[float]":

        """
            Function to plot the normalied histogram of the data and the probability
            density function.

            Args:
                n_spaces (int): number of data points to plot
            
            Returns:
                list[float]: x values for pdf plot
                list[float]: y values for pdf plot

        """

        mean, stdev, min_range, max_range = self.mean, self.stdev, min(self.data), max(self.data)

        # Calculate the interval between x values
        interval = 1.0 * (max_range - min_range) / n_spaces

        # Calcuate the x values for ploting
        _x = [min_range + interval * x for x in range(n_spaces)]
        _y = [self.pdf(x) for x in _x]

        # Create the plots
        fig, axes = plt.subplots(ncols=1, nrows=2, sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normalized Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(_x, _y)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[1].set_ylabel('Density')
        plt.show()

        return _x, _y

    def __add__(self, other: type) -> type:
        """
            Function to add together two Gaussian distributions.

            Args:
                other (Gaussian): A instance of the Gaussian class.
            
            Returns:
                type (Gaussian): Combination of the two Gaussian distributions as a Gaussian instance.
        
        """
        
        result = Gaussian()
        result.mean = self.mean + other.mean
        result.stdev = math.sqrt((self.stdev ** 2) + (other.stdev ** 2))

        return result

    def __repr__(self):
        """
            Function to return the characteristics of the Gaussian instance.

            Args:
                None
            
            Returns:
                str: characteristics of the Gaussian instance.
        
        """

        return f'Mean: {self.mean}, Standard Deviation: {self.stdev}, N: {self.n}'
