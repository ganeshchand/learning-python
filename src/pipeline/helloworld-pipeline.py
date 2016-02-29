import luigi


class HelloWorldTask(luigi.Task):
    # def requires(self):
    #	"""nothing"""

    # def output(self):
    # """nothing"""
    # return ""

    def run(self):
        print("{taskName} says: Hello World!".format(taskName=self.__class__.__name__))


if __name__ == '__main__':
    luigi.run()
