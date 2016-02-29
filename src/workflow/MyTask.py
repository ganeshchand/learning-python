import luigi


class MyTask(luigi.Task):
    def run(self):
        print("hello, world")

    def output(self):
        print("hello, world")


if __name__ == '__main__':
    luigi.run(main_task_cls=MyTask)
