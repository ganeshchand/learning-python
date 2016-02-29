import luigi


class Task0(luigi.Task):

    def output(self):
        return {"output of Task0"}

    def run(self):
        print("Ran task0")


class Task1(luigi.Task):
    def requires(self):
        Task0()

    def output(self):
        return {"output of Task1"}

    def run(self):
        print("task1")
        print(self.input() + self.output())

if __name__ == '__main__':
    luigi.run()
