import luigi


class InputText(luigi.ExternalTask):
    date = luigi.DateParameter()

    def output(self):
        print("Task {} is running.".format(self.__class__.__name__))
        return luigi.LocalTarget(self.date.strftime('/tmp/text/%Y-%m-%d.txt'))


class WordCount(luigi.Task):
    dateInterval = luigi.DateIntervalParameter()

    def requires(self):
        """
        This task dependencies:
        * :py:class: `~.InputText`

        :return: list of object (:py:class: `luigi.task.Task`)
        """

        return [InputText(date) for date in self.dateInterval.dates()]

    def output(self):
        print("Task {} is running.".format(self.__class__.__name__))
        return luigi.LocalTarget('/tmp/text/text-count/%s' % self.dateInterval)

    def run(self):
        """
        1. Count the words for each of the :py:meth:`~.InputText.output` targets created by :py:class:`~.InputText`
        2. write the count into the :py:meth:`~.WordCount.output` target
        """

        count = {} # empty dictionary

        for f in self.input(): # The input method is a wrapper around requires() that returns Target objects
            for line in f.open('r'):
                for word in line.strip().split():
                    count[word] = count.get(word,0) + 1


        # output data
        f = self.output().open('w')
        for word, count in luigi.six.iteritems(count):
            f.write("%s\t%d\n" % (word, count))

        f.close()





if __name__ == '__main__':
    luigi.run()
