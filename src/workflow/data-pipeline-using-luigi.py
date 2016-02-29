import luigi
import tempfile
import os

# There are two core concepts in Luigi: Tasks and Targets
# Targets:
"""
Targets: Broadly speaking, the Target class corresponds to a file on a disk. Or a file on S3.
Or some kind of a checkpoint, like an entry in a database.
The only method that Targets have to implement is the exists method, which returns True if and only
if the Target exists.
LocalTarget, S3Target, or FTPTarget classes that are available out of the box.
"""
# Targets:
"""
The Task class is where work gets done in Luigi. It has a very simple interface, with only three methods
you need to implement: requires, output, and run.
"""

# Pipeline
"""
This data pipeline has two tasks:
    PrintNumbers - writes the number from 1 to 10 into a file called numbers_up_to_10.txt
    SquaredNumbers that reads numbers_up_to_10.txt and outputs a list of pair number-square into squares.txt

"""


class PrintNumbers(luigi.Task):
    def requires(self):  # should return the list of dependencies for the given task
        return []

    def output(self):  # should return the target for the task (e.g. a LocalTarget, a S3Target, etc.)
        outputFilePath = tempfile.gettempdir() + os.path.sep + "number_up_to_10.txt"
        print("Output path is {}".format(outputFilePath))
        return luigi.LocalTarget(outputFilePath)

    def run(self):  # should contain the logic to execute
        print("Running PrintNumbers...")
        with self.output().open('w') as f:
            for i in range(1, 11):
                f.write("{}\n".format(i))

class SquaredNumbers(luigi.Task):
    def requires(self):
        return [PrintNumbers]

    def output(self):
        outputFilePath = tempfile.gettempdir() + os.path.sep + "square.txt"
        print("Output path is {}".format(outputFilePath))
        return luigi.LocalTarget(outputFilePath)

    def run(self):
        with self.input()[0].open() as fin, self.output().open('w') as fout:
            for line in fin:
                n = int(line.strip())
                out = n * n
                fout.write("{}: {}\n".format(n, out))


if __name__ == '__main__':
    luigi.run(main_task_cls=SquaredNumbers)

    # To run the tasks: $ Python data-pipeline-using-luigisample.py SquaredNumbers -- local-scheduler
