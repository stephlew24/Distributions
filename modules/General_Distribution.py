# %%

class Distribution():

    def __init__(self, mean: float = 0, stdev: float = 0) -> None:

        """ 
            Class to calculate and visualize distributions
    
            Attributes:
                mean (float) calculates the mean value of the distribution
                stdev (float) calculates the standard deviation of the distribution
                data (list[float]) a list of floats extracted from the data file

        """

        self.mean = mean
        self.stdev = stdev

    def read_data_file(self, file_name: str) -> 'list[float]':

        """ 
            Method to read a txt format data file. This file should have one number(float) per line. 
            The numbers are stored in the data attribute.

            Args:
                file_name (str): name of a file to read.

            Returns:
                None

        """

        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()
        file.close()

        self.data = data_list

        if isinstance(self.data, list) and len(self.data) > 0:
            print("Data loaded properly.")
        else:
            print("There was a problem, please try again.")
        
        return self.data