import os
import luigi


class PrepareOutputDir(luigi.Task):
    """
    If invoked, it cleans up existing files. Also, creates required directories.
    """

    # outputDir = luigi.Parameter()
    # fileName = luigi.Parameter()
    # cleanAndPrepareOutputDir = luigi.BoolParameter(default=False)
    #
    # outputPath = str(outputDir) + os.sep + str(fileName)

    # Doesn't depend on any other task

    def output(self):
        # print(self.outputDir)
        return luigi.LocalTarget("tmp/test.txt")  # self.outputPath

        # def run(self):
        #     if self.cleanAndPrepareOutputDir:  # Run only if asked to clean existing output file
        #         if os.path.exists(self.outputDir):  # check if dir exists
        #             if os.path.exists(self.outputPath):  # check if file exists
        #                 os.remove(self.outputPath)
        #             else:  # just delete the directory
        #                 os.removedirs(self.outputDir)
        #         else:  # create required directories
        #             os.mkdirs(self.outputDir)
        #     return self.outputPath


class MyTask(luigi.Task):
    def requires(self):
        PrepareOutputDir()

    def run(self):
        print("My Task")
        myinput = self.input()
        print("Return Type : {}".format(myinput))
        # print(type(self.input()))


if __name__ == '__main__':
    luigi.run()
