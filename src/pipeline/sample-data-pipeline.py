import luigi
import os, inspect
from os import listdir


# Task1: Read a csv file

# Task2: Filter some lines

# Task3: Aggregate Data

# Task4: Save Output in a file


# Task1: Load data from files
class ReadInputFile(luigi.ExternalTask):
    """
    This class represents something that was created elsewhere by an external process.
    So, we just need to implement the output method.
    """

    fileName = luigi.parameter

    def output(self):
        """ Returns the target output for this task. In this case, it expects a file to be present in the local file system.
        :return: the target output for this task.
        :rtype: object(:py:class: 'luigi.target.Target')
        """

        # The directory containing this file
        print("Runing Task: ".format(self.__class__.__name__))

        root = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + os.pathsep
        return luigi.LocalTarget(root + self.fileName)


# Task 2: Filter Data
class FilterData(luigi.Task):
    def requires(self):
        return [ReadInputFile(self.input_dir + os.pathsep + self.filename)
                for filename in listdir(self.input_dir)]

    def output(self):
        targets = [luigi.LocalTarget('output/filteredData.csv')]
        return targets

    def run(self):
        print("Runing Task: ".format(self.__class__.__name__))


if __name__ == "__main__":
    luigi.run

