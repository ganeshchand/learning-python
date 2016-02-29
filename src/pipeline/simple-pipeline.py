import luigi
import os

"""
To run:
    python simple-pipeline.py MyTask --local-scheduler
"""


class InputText(luigi.ExternalTask):
    """
    A Luigi Task - It wraps a Target Object
    This task assumes there is an input text file created at a given path.
    It just returns the input file path
    """

    def output(self):
        """
        :return: absolute input file path
        """
        return luigi.LocalTarget("/etc/passwd")


class PrepareOutputDir(luigi.Task):
    """
    If invoked, it cleans up existing files. Also, creates required directories.
    """
    outputDir = "/tmp/python/output"  # luigi.Parameter()
    fileName = "user-names.txt"  # luigi.Parameter()
    cleanAndPrepareOutputDir = luigi.BoolParameter(default=False)

    outputPath = str(outputDir) + os.sep + str(fileName)

    # Doesn't depend on any other task

    def output(self):
        return self.outputPath

    def run(self):
        if self.cleanAndPrepareOutputDir:  # Run only if asked to clean existing output file
            if os.path.exists(self.outputDir):  # check if dir exists
                if os.path.exists(self.outputPath):  # check if file exists
                    os.remove(self.outputPath)
                else:  # just delete the directory
                    os.removedirs(self.outputDir)
            else:  # create required directories
                os.mkdirs(self.outputDir)


class ExtractUserName(luigi.Task):
    cleanAndPrepareOutputDir = luigi.BoolParameter(default=False)

    # outputDir = luigi.Parameter()
    # fileName = luigi.Parameter()

    def requires(self):
        if PrepareOutputDir.cleanAndPrepareOutputDir:
            return {"InputText": InputText(),
                    "PrepareOutputDir": PrepareOutputDir(self.cleanAndPrepareOutputDir)}
        else:
            {"InputText": InputText()}

    def output(self):
        return luigi.LocalTarget("/tmp/python/output/user-names.txt")

    def run(self):
        """
        Run this task
        :return:
        """

        # Open the files specified by requires() and output() respectively
        ifp = self.input()['InputText'].open('r')
        ofp = self.output().open('w')

        # Put each username in the output file along with new line character
        import os
        newLineChar = os.linesep

        for line in ifp:
            name = line.strip().split(':')[0]  # we want only the user names
            if not name.startswith("#"):  # ignore comment lines
                ofp.write("{}{}".format(name, newLineChar))
        ofp.close()
        ifp.close()


if __name__ == '__main__':
    luigi.run(main_task_cls=ExtractUserName)
