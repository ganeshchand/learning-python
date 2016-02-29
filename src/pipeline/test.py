import os
import os.path
import luigi


class PrepareOutputDir(luigi.Task):
    outputDir = luigi.Parameter()
    fileName = luigi.Parameter()

    def outputFilePath(self):
        return os.path.join(self.outputDir, self.fileName)

    def output(self):
        return luigi.LocalTarget(self.outputFilePath())

    def run(self):

        # create a directory
        if not os.path.exists(self.outputDir):
            os.makedirs(self.outputDir)
        # create a file
        if not os.path.exists(self.outputFilePath()):
            f = open(self.outputFilePath(), 'w')
            f.close()


class MyTask(luigi.Task):
    def requires(self):
        return PrepareOutputDir()

    def run(self):
        with self.input().open('w') as f:
            f.write("Sucess!!\n")


if __name__ == '__main__':
    luigi.run()
